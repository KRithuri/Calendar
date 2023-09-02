const date = new Date();
const renderCalendar = () => {
    date.setDate(1);
    const monthDays = document.querySelector(".days");

    const lastDate = new Date(
        date.getFullYear(),
        date.getMonth() + 1,
        0
    )
}