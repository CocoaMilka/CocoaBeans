function deleteCommission(commissionID)
{
    fetch("/delete-commission", {
        method: "POST",
        body: JSON.stringify({ commissionID: commissionID}),
    }).then((_res) => {
        window.location.href = "/";
    })
}