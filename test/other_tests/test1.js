// test 2   uporabimo navigation
const token = "3596223707";

async function navigate(fromPage, toPage) {
  const url = 'https://192.168.3.50/PIC6/api/user_navigation_history/savenavigationhistory';
  const payload = {"fromPage":fromPage,"toPage":toPage,"userAccessLevel":"NONE","timestamp":1702820981960,"currentMobileOS":"unknown","token":token};
  //const response = await fetch(url, {
  return await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    }).then(res => {
      console.log(res.json());
      console.log(res.status);
    })
    .catch(err => console.error(err));
}

async function fetch_some_data() {
  const url = 'https://192.168.3.50/PIC6/api/menu/getmenutable';
  const payload = { "token": token };
  return await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    }).then(res => console.log(res.json()))
    .catch(err => console.error(err));
}

await navigate("Home - CARRIER 30XW", "Main Menu");
await navigate("Main Menu", "Menu_Target_Status_Table");
await fetch_some_data();

/* NE DELA, dobimo
200
200
500 { error: "Failed to get data from menu generation table!", status: "0" }
*/