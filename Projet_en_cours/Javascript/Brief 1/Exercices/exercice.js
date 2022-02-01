/*

let a = 10;
let b = 5;
let c = 1;


let test = prompt("Merci d'inscrire une chaine de caractères ?");
document.body.innerHTML = test;


let result = a + b;
alert(result);


let note_maths = 11;
let note_francais = 9;
let note_hg = 16;
let moyenne = (note_maths + note_francais + note_hg ) / 3 ;
alert('La moyenne est de ' + moyenne);


let budget = 1500;
let achats = 270;

if (budget >= achats)
    console.log("le budget de " + budget + " permet les achats de " + achats);
else
    console.log("le budget de " + budget + " ne permet pas les achats de " + achats);


let prixHT = prompt("Merci d'inscrire une somme HT ?");
let prixTVA = prixHT * 1.2
document.body.innerText = prixTVA;
 
let prixHT2 = prompt("Merci d'inscrire une somme HT ?");
let prixTVA2 = prompt("Merci d'inscrire un taux de TVA?");
let prixTTC = prixHT2 * (1 + prixTVA2/100);
document.body.innerText = prixTTC;


let prixHT3 = prompt("Merci d'inscrire une somme HT ?");
let prixTVA3 = prompt("Merci d'inscrire un taux de TVA?");
let prixTTC3 = prixHT3 * (1 + prixTVA3/100);
document.body.innerHTML = prixTTC3;

if(prixTTC3 > 100) {
    document.body.innerHTML = '<h1 style="color: red;">' + prixTTC3 + '</h1>';
} else {
    document.body.innerHTML = '<h1 style="color: green;">' + prixTTC3 + '</h1>';
}


document.getElementById('cocktail').innerText = 'Long Island Iced Tea';


for(let multiple = 10;multiple <= 1000;multiple+= 10) {
    console.log('table ' + multiple);
    }



let age = prompt("Quel âge avez-vous ? ")
if (age > 18)
    alert("Vous êtes majeur.")
else
    alert("Vous êtes mineur.")

    

let dep = 0;
while (dep < 1000){
    if (dep < 10){
        console.log("7700" + dep);
        dep ++;
    }
    else if (dep < 100) {
        console.log("770" + dep);
        dep ++;
    }
    else{
        console.log("77" + dep);
        dep ++;
    }
}



let somme = ""
for(let table_cinq = 5; table_cinq <= 50; table_cinq += 5){
    somme = somme + "la table de cinq : " + table_cinq + '\n';
}
document.body.innerHTML = somme;

*/

let somme = "";
for(let i = 1; i < 6; i++){
        for(let k = 1; i< 6; k++){
            somme = somme + k + '\n';
    }
    somme = somme + i + '\n';
}
document.body.innerHTML = somme;
