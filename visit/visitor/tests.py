# if (document.querySelector('input[name="{{ form.parking.name }}"]')) {
#
#         const parkingCheckbox = document.querySelector('input[name="{{ form.parking.name }}"]');
#         const parkingChoice = document.getElementById("parking_choice");
#
#         if (parkingCheckbox) {
#             parkingCheckbox.addEventListener('change', function () {
#                 if (parkingCheckbox.checked) {
#                     parkingChoice.style.display = 'inline';
#                 } else {
#                     parkingChoice.style.display = 'none';
#                 }
#             });
#         }
#     }
#     if (document.querySelector('input[name="{{ form.needs_shoes.name }}"]')) {
#         const shoesCheckbox = document.querySelector('input[name="{{ form.needs_shoes.name }}"]');
#         const inputSizeShoes = document.getElementById("size_shoes");
#         if (shoesCheckbox) {
#             shoesCheckbox.addEventListener('change', function () {
#                 if (shoesCheckbox.checked) {
#                     inputSizeShoes.style.display = 'inline';
#                 } else {
#                     inputSizeShoes.style.display = 'none';
#                 }
#             });
#         }
#     }
#     if (document.getElementById('restaurant_info')) {
#         document.addEventListener('DOMContentLoaded', function () {
#             const restaurantInfo = document.getElementById('restaurant_info');
#             const reservationCheckbox = document.querySelector('input[name="reservation"]');
#
#             reservationCheckbox.addEventListener('change', function () {
#                 if (reservationCheckbox.checked) {
#                     restaurantInfo.style.display = 'block';
#                     const restaurantOthers = document.getElementById('restaurant_others');
#                     const othersCheckbox = document.querySelector('input[name="others"]');
#                     othersCheckbox.addEventListener('change', function () {
#                         if (othersCheckbox.checked) {
#                             restaurantOthers.style.display = 'block';
#                         } else {
#                             restaurantOthers.style.display = 'none';
#                         }
#                     });
#                 } else {
#                     restaurantInfo.style.display = 'none';
#                 }
#             });
#         })
#     }
#
#
#     if (document.getElementById('out_meeting_info')) {
#         document.addEventListener("DOMContentLoaded", function () {
#             const outMeetingInfo = document.getElementById('out_meeting_info');
#             const meetingCheckbox = document.querySelector('input[name="meeting"]');
#             meetingCheckbox.addEventListener('change', function () {
#                 if (meetingCheckbox.checked) {
#                     outMeetingInfo.style.display = 'block';
#                     const transportCheckbox = document.querySelector('input[name="transport"]');
#                     const meetingTrChoice = document.querySelector('.meeting_tr_choice');
#                     const tr_choice_meeting = document.querySelector('#meeting_tr_choice_btn')
#
#                     transportCheckbox.addEventListener('change', function () {
#                         if (transportCheckbox.checked) {
#                             meetingTrChoice.style.display = 'block';
#                             tr_choice_meeting.style.display = 'block';
#                         } else {
#                             meetingTrChoice.style.display = 'none';
#                             tr_choice_meeting.style.display = 'none';
#                         }
#                     });
#                 } else {
#                     outMeetingInfo.style.display = 'none';
#                 }
#             });
#         })
#     }
#
#
#     if (document.querySelector('input[name="another_visitor"]')) {
#         console.log(document.querySelector('input[name="another_visitor"]'))
#         const anotherVisitorCheckbox = document.querySelector('input[name="another_visitor"]');
#         const addVisitorDiv = document.getElementById('add_visitor');
#
#         anotherVisitorCheckbox.addEventListener('change', function () {
#             if (anotherVisitorCheckbox.checked) {
#                 addVisitorDiv.style.display = 'block';
#             } else {
#                 addVisitorDiv.style.display = 'none';
#             }
#         })
#     }
#
#    document.addEventListener("DOMContentLoaded", function () {
#     const visitorSelect = document.getElementById('visitorSelect');
#     const card_visitor_info = document.getElementById('card_visitor');
#     const card_transport_visitor = document.getElementById('card_transport');
#     const card_accommodation = document.getElementById('card_accommodation');
#     const card_security_safety = document.getElementById('card_security_safety');
#     const card_meeting_room = document.getElementById('card_meeting_room');
#     const card_catering = document.getElementById('card_catering');
#     const card_addition_vis = document.getElementById('card_addition_vis');
#     const card_other_req = document.getElementById('card_other_req');
#     const card_meeting_planner = document.getElementById('card_meeting_planner');
#     const card_restaurant_reservation = document.getElementById('card_restaurant_reservation');
#
#     function clearCardContents() {
#         card_security_safety.innerHTML = '';
#         card_visitor_info.innerHTML = '';
#         card_accommodation.innerHTML = '';
#         card_transport_visitor.innerHTML = '';
#         card_meeting_room.innerHTML = '';
#         card_catering.innerHTML = '';
#         card_addition_vis.innerHTML = '';
#         card_other_req.innerHTML = '';
#         card_meeting_planner.innerHTML = '';
#         card_restaurant_reservation.innerHTML = '';
#     }
#
#     function handleCategory(card, values) {
#         if (values[0]) {
#             const categoryValues = values[0];
#             for (const [catKey, catValue] of Object.entries(categoryValues)) {
#                 if (catKey === 'id' || catKey === 'visitor_id' || catValue == null || catValue === false || catValue === '') {
#                     continue;
#                 }
#                 const listItem = document.createElement('li');
#                 const textNode = document.createTextNode(`${catKey}  :  ${catValue}`);
#                 listItem.appendChild(textNode);
#                 card.appendChild(listItem);
#             }
#         }
#     }
#
#     visitorSelect.style.border = "1px solid #ccc";
#     visitorSelect.style.borderRadius = "5px";
#
#     visitorSelect.addEventListener("change", function () {
#         const selectedValue = visitorSelect.value;
#         clearCardContents();
#
#         if (selectedValue) {
#             fetch(`get_visitor_info/${selectedValue}/`)
#                 .then(response => {
#                     if (!response.ok) {
#                         throw new Error('Грешка при извличането на информацията за посетителя.');
#                     }
#                     return response.json();
#                 })
#                 .then(data => {
#                     const visitorData = data;
#                     for (const [vkey, vvalue] of Object.entries(visitorData)) {
#                         for (const [visitorKey, visitorValue] of Object.entries(vvalue)) {
#                             if (visitorKey !== "id" && !Array.isArray(visitorValue)) {
#                                 const listItem = document.createElement('li');
#                                 const textNode = document.createTextNode(`${visitorKey}: ${visitorValue}`);
#                                 listItem.appendChild(textNode);
#                                 card_visitor_info.appendChild(listItem);
#                             } else {
#                                 if (visitorKey === 'transportation') {
#                                     handleCategory(card_transport_visitor, visitorValue);
#                                 } else if (visitorKey === 'accommodation') {
#                                     handleCategory(card_accommodation, visitorValue);
#                                 } else if (visitorKey === 'safety_needs' || visitorKey === "security_info") {
#                                     handleCategory(card_security_safety, visitorValue);
#                                 } else if (visitorKey === 'visitor_meeting') {
#                                     handleCategory(card_meeting_room, visitorValue);
#                                 } else if (visitorKey === 'visitor_catering') {
#                                     handleCategory(card_catering, visitorValue);
#                                 } else if (visitorKey === 'visitor_out_office') {
#                                     handleCategory(card_meeting_planner, visitorValue);
#                                 } else if (visitorKey === 'visitor_restaurant') {
#                                     handleCategory(card_restaurant_reservation, visitorValue);
#                                 } else if (visitorKey === 'visitor_others' || visitorKey === 'visitor_additional') {
#                                     handleCategory(card_addition_vis, visitorValue);
#                                 }
#                             }
#                         }
#                     }
#                 })
#                 .catch(error => {
#                     alert(error.message);
#                 });
#
#             const deleteButton = document.querySelector('.del-btn')
#             deleteButton.addEventListener("click", function () {
#                 if (selectedValue) {
#                     deleteButton.setAttribute("disabled", "disabled");
#                     fetch(`delete_visitor/${selectedValue}`)
#                         .then(deleteResponse => {
#
#                             if (deleteResponse.status === 200) {
#                                 alert("Посетителят е изтрит успешно.")
#                                 clearCardContents()
#                                 location.reload()
#                             } else {
#                                 alert("Възникна проблем при изтриването.");
#                             }
#                         })
#                         .catch(error => {
#                             console.error('Грешка при изтриването на посетителя:', error);
#                         });
#                 } else {
#                     alert("Моля, изберете посетител, когото да изтриете.");
#                 }
#             });
#         } else {
#             clearCardContents();
#         }
#     });
# });
#
# document.addEventListener("DOMContentLoaded", function () {
#     const visitorSelect = document.getElementById('visitorSelect');
#     const editButton = document.querySelector('.edit-button');
#
#     visitorSelect.addEventListener("change", function () {
#         const selectedValue = visitorSelect.value;
#         if (selectedValue) {
#             editButton.href = `edit_visitor/${selectedValue}`;
#         } else {
#
#             editButton.href = "#";
#         }
#     });
# });
#
#     const othersCheckbox = document.querySelector('input[name="{{ form.room_others.name }}');
#
#     const formGroupOthers = document.getElementById("meeting_r_others");
#
#     if (othersCheckbox.checked) {
#          formGroupOthers.style.display = 'inline';
#          othersCheckbox.addEventListener('change', function () {
#             if (othersCheckbox.checked) {
#                 formGroupOthers.style.display = 'block';
#             } else {
#                 formGroupOthers.style.display = 'none';
#             }
#         });
#     }else {
#             formGroupOthers.style.display = 'none';
#
#     }