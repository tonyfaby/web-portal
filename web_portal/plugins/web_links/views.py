from quart import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from quart_auth import current_user, login_required
from web_portal.database import models as app_models
from web_portal.helpers import login_admin_required

from . import models

blueprint = Blueprint("web_links", __name__, template_folder="templates")


@blueprint.get("/links")
@login_admin_required
async def get_links():
    links = await models.Link.all()
    return await render_template(
        "web_links/links.jinja",
        links=links
    )


@blueprint.get("/links/new")
@login_admin_required
async def get_link_new():
    return await render_template("web_links/links/new.jinja")


@blueprint.post("/links/new")
@login_admin_required
async def post_link_new():
    form = await request.form

    name = form["name"].strip()
    url = form["url"].strip()
    color_name = form["color_name"].strip()

    await models.Link.create(
        name=name,
        url=url,
        color_name=color_name,
    )

    await flash(f"created link with name '{name}'", "green")

    return redirect(url_for(".get_links"))


# HACK this does not handle any other widget that 'link'
@blueprint.get("/widget/<int:widget_id>")
@login_required
async def get_widget(widget_id: int):
    widget = await app_models.DashboardWidget.get(id=widget_id).prefetch_related("dashboard")

    if widget.dashboard.owner_id != current_user.auth_id:
        abort(401)

    links = await models.Link.all()
    added_links = await models.Link.filter(id__in=widget.config["links"]).all()

    return await render_template(
        "web_links/widget.jinja",
        added_links=added_links,
        links=links,
        widget_id=widget_id,
    )


# HACK this does not handle any other widget that 'link'
@blueprint.post("/widget/<int:widget_id>/add-link")
@login_required
async def post_widget_add_link(widget_id: int):
    widget = await app_models.DashboardWidget.get(id=widget_id).prefetch_related("dashboard")

    if widget.dashboard.owner_id != current_user.auth_id:
        abort(401)

    link_id = await request.form["link-id"]
    _ = await models.Link.get(id=link_id)

    if widget.config is None:
        widget.config = {"links": []}

    widget.config["links"].append(link_id)

    await widget.save()

    return redirect(url_for(".get_widget", widget_id=widget_id))
