// if (document.querySelector('input[name="{{ form.parking.name }}"]')) {
//
//     const parkingCheckbox = document.querySelector('input[name="{{ form.parking.name }}"]');
//     const parkingChoice = document.getElementById("parking_choice");
//
//     if (parkingCheckbox) {
//         parkingCheckbox.addEventListener('change', function () {
//             if (parkingCheckbox.checked) {
//                 parkingChoice.style.display = 'inline';
//             } else {
//                 parkingChoice.style.display = 'none';
//             }
//         });
//     }
// }
// if (document.querySelector('input[name="{{ form.needs_shoes.name }}"]')) {
//     const shoesCheckbox = document.querySelector('input[name="{{ form.needs_shoes.name }}"]');
//     const inputSizeShoes = document.getElementById("size_shoes");
//     if (shoesCheckbox) {
//         shoesCheckbox.addEventListener('change', function () {
//             if (shoesCheckbox.checked) {
//                 inputSizeShoes.style.display = 'inline';
//             } else {
//                 inputSizeShoes.style.display = 'none';
//             }
//         });
//     }
// }
// if (document.getElementById('restaurant_info')) {
//     document.addEventListener('DOMContentLoaded', function () {
//         const restaurantInfo = document.getElementById('restaurant_info');
//         const reservationCheckbox = document.querySelector('input[name="reservation"]');
//
//         reservationCheckbox.addEventListener('change', function () {
//             if (reservationCheckbox.checked) {
//                 restaurantInfo.style.display = 'block';
//                 const restaurantOthers = document.getElementById('restaurant_others');
//                 const othersCheckbox = document.querySelector('input[name="others"]');
//                 othersCheckbox.addEventListener('change', function () {
//                     if (othersCheckbox.checked) {
//                         restaurantOthers.style.display = 'block';
//                     } else {
//                         restaurantOthers.style.display = 'none';
//                     }
//                 });
//             } else {
//                 restaurantInfo.style.display = 'none';
//             }
//         });
//     })
// }
//
//
// if (document.getElementById('out_meeting_info')) {
//     document.addEventListener("DOMContentLoaded", function () {
//         const outMeetingInfo = document.getElementById('out_meeting_info');
//         const meetingCheckbox = document.querySelector('input[name="meeting"]');
//         meetingCheckbox.addEventListener('change', function () {
//             if (meetingCheckbox.checked) {
//                 outMeetingInfo.style.display = 'block';
//                 const transportCheckbox = document.querySelector('input[name="transport"]');
//                 const meetingTrChoice = document.querySelector('.meeting_tr_choice');
//                 const tr_choice_meeting = document.querySelector('#meeting_tr_choice_btn')
//
//                 transportCheckbox.addEventListener('change', function () {
//                     if (transportCheckbox.checked) {
//                         meetingTrChoice.style.display = 'block';
//                         tr_choice_meeting.style.display = 'block';
//                     } else {
//                         meetingTrChoice.style.display = 'none';
//                         tr_choice_meeting.style.display = 'none';
//                     }
//                 });
//             } else {
//                 outMeetingInfo.style.display = 'none';
//             }
//         });
//     })
// }
//
//
// if (document.querySelector('input[name="another_visitor"]')) {
//     console.log(document.querySelector('input[name="another_visitor"]'))
//     const anotherVisitorCheckbox = document.querySelector('input[name="another_visitor"]');
//     const addVisitorDiv = document.getElementById('add_visitor');
//
//     anotherVisitorCheckbox.addEventListener('change', function () {
//         if (anotherVisitorCheckbox.checked) {
//             addVisitorDiv.style.display = 'block';
//         } else {
//             addVisitorDiv.style.display = 'none';
//         }
//     })
// }
//
// if (document.getElementById('visitorSelect')) {
//     const visitorSelect = document.getElementById('visitorSelect');
//     const card_visitor_info = document.getElementById('card_visitor')
//     const card_transport_visitor = document.getElementById('card_transport')
//     const card_accommodation = document.getElementById('card_accommodation')
//     const card_security_safety = document.getElementById('card_security_safety')
//     const card_meeting_room = document.getElementById('card_meeting_room')
//     const card_catering = document.getElementById('card_catering')
//     const card_meeting_planner = document.getElementById('card_meeting_planner')
//     const card_restaurant_reservation = document.getElementById('card_restaurant_reservation')
//     const card_other_req = document.getElementById('card_other_req')
//     const card_addition_vis = document.getElementById('card_addition_vis')
//
//
//     document.addEventListener("DOMContentLoaded", function () {
//         const selectElement = document.getElementById("visitorSelect");
//
//
//         selectElement.style.padding = "10px";
//         selectElement.style.border = "1px solid #ccc";
//         selectElement.style.borderRadius = "5px";
//
//
//         selectElement.addEventListener("change", function () {
//
//             const selectedValue = selectElement.value;
//             console.log("Избрана стойност:");
//         });
//     })
// }
//
//
