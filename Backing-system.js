// Bank system
// data base
const accounts = []

// creat account
function createAccounts(name, initialBalance) {
    if (initialBalance < 0) {
        console.log("initial balance cannot be negative")
        return;
    }

    const account = {
        id: accounts.length + 1,
        name: name,
        balance: initialBalance
    };

    accounts.push(account);
    console.log(`Account created successfully. Account ID: ${account.id}, Name: ${account.name}, Balance: ${account.balance}`);
    return account;
}
createAccounts("amin", 1000)

// deposit
function deposit(accountId, amount) {
    // get id from database
    const account = accounts.find(acc => acc.id === accountId) 
if(!account) {
    console.log("account not found")
    return;
}
if(amount <=0){
    console.log("amount cannot be negative")
    return;
}
account.balance += amount  //balance =balbnce + amount 

console.log(`Deposit is success :${amount} the new balance is ${account.balance}`);
// return account
}

// withdraw
function withdraw(accountId, amount) {
    const account =accounts.find(acc => acc.id === accountId)
    if(!account) {
        console.log("account not found")
        return;
    }
    if(amount<=0){
        console.log("amount cannot be negative")
        return;
    }
    if(amount > account.balance){
        console.log("insufficient balance")
        return;
    }
    account.balance -= amount // balance  =balance - amount
    console.log(`withdraw is success :${amount}the new balance is ${account.balance}`)

}
// check balance
function checkBalance(accountId){
    const account =accounts.find(acc => acc.id === accountId)
    if(!account) {
        console.log("account not found")
        return;
    }
    console.log(`the balance is ${account.balance}`)
}
//view account
function viewAccount(){
    if(accounts.length ===0) {
        console.log("account not found")
        return;
    }
console.log("all accounts:")
accounts.forEach(account => {
    console.log(`ID: ${account.id}, Name: ${account.name}, Balance: ${account.balance}`)
})
}


createAccounts("mariam", 1000)
deposit(1, 500)
withdraw(1, 600)
checkBalance(1)
deposit(1, 750)
checkBalance(1)


createAccounts("amin", 900)
deposit(2, 3098)
withdraw(2, 678)
checkBalance(2)
deposit(2, 5667)
checkBalance(2)
viewAccount()