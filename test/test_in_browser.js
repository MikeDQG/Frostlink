//   tu so testi, ki jih med izvajanjem spletne strani v browserju kopiramo v console in klicemo fetch()

async function fetch_some_data() {  // test doma, da vidim princip
    const url = 'https://arriva.si/vozni-redi/?departure-1102=Slovenska+Bistrica&departure_id=140455&departure=Slovenska+Bistrica&destination=Maribor+AP&destination_id=139129&trip_date=05.01.2024'
    const response = await fetch(url).then(res => res.json());
    return response;
}


// test 1   poskusimo dobiti podatke iz tabele
async function fetch_some_data(token) {
    const url = 'https://192.168.3.50/PIC6/api/menu/getmenutable';
    const payload = { "token": token };
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
/* // test v GEA, NE DELA,                    ^^^^^^^^^^^^^^^^^
sporocilo je spet isto: 
{ error: "Failed to get data from menu generation table!", status: "0" }
*/


