from datetime import datetime


def build_subject():
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    return f"AWS ASG CPU Metrics Report - {date_str}"


def build_html(owner_name, asg_reports):
    asg_sections = ""

    for asg in asg_reports:

        # ---------- ASG METADATA ----------
        metadata = f"""
        <h3>ASG: {asg['name']}</h3>
        <p>
        <b>Region:</b> {asg['region']} <br>
        <b>Created (IST):</b> {asg['created']} <br>
        <b>Capacity (min/desired/max):</b> {asg['capacity']}
        </p>
        """

        # ---------- HOURLY TABLE ----------
        rows = ""
        for m in asg["metrics"]:
            rows += f"""
            <tr>
                <td>{m['time']}</td>
                <td>{m['avg_cpu']}%</td>
                <td>{m['max_cpu']}%</td>
            </tr>
            """

        table = f"""
        <table border="1" cellpadding="6" cellspacing="0">
            <tr>
                <th>Hour (IST)</th>
                <th>Avg CPU</th>
                <th>Max CPU</th>
            </tr>
            {rows}
        </table>
        <br>
        """

        asg_sections += metadata + table

    html = f"""
    <html>
    <body>
        <h2>Hello {owner_name},</h2>
        <p>Here is your ASG hourly CPU utilization report (last 24h):</p>

        {asg_sections}

        <p>Please review and take action if required.</p>
    </body>
    </html>
    """

    return html
