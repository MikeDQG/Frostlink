//  test z getPointValue
const token = "793465726359";
async function fetch_some_data() {
    const url = 'https://192.168.3.50/PIC6/api/point_value/getpointvalue';
    const payload = {"pathlist":[{"widgetType":"PointValue","path":"db/Ui_Alias_COND_EWT/present-value"},{"widgetType":"PointValue","path":"db/Ui_Syn_Msg_Bottom/description"},{"widgetType":"PointValue","path":"db/Ui_Alias_CTRL_PNT/present-value"},{"widgetType":"PointValue","path":"db/Ui_Alias_OAT/present-value"},{"widgetType":"PointValue","path":"db/Ui_Alias_CAP_T/present-value"},{"widgetType":"PointValue","path":"db/Ui_Alias_unit_typ/present-value"},{"widgetType":"PointValue","path":"db/CTRLID_DEV_LOCATION/active-text"},{"widgetType":"PointValue","path":"db/Ui_Alias_FLOW_SW/present-value"},{"widgetType":"PointValue","path":"db/Ui_Alias_EWT/present-value"},{"widgetType":"PointValue","path":"db/Ui_Alias_LWT/present-value"},{"widgetType":"PointValue","path":"db/Ui_Alias_COND_LWT/present-value"},{"widgetType":"PointValue","path":"db/Ui_runtest_ip/active-text"},{"widgetType":"PointValue","path":"db/Ui_runtest_mask/active-text"},{"widgetType":"PointValue","path":"db/Ui_runtest_eth/active-text"}],
    "token":token}
    //const response = await fetch(url, {
    return await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      }).then(res => console.log(res.json()))
      .catch(err => console.error(err));
}