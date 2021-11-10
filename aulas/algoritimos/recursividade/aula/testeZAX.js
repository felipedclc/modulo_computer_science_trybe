// Quando eu executar o script passando apenas o motoboy ou não passando nenhum motoboy, preciso ver:
// Quem é o motoboy e quantos pedidos terá?
// De qual loja é?
// Quanto vai ganhar?

const store1 = { requests: [{ pedido1: 50.00, pedido2: 50.00, pedido3: 50.00 }], percentageTax: 5 };
const store2 = { requests: [{ pedido1: 50.00, pedido2: 50.00, pedido3: 50.00, pedido3: 50.00 }], percentageTax: 5 };
const store3 = { requests: [{ pedido1: 50.00, pedido2: 50.00, pedido3: 100.00 }], percentageTax: 15 };

const moto1 = { price: 2.00, exclusive: false };
const moto2 = { price: 2.00, exclusive: false };
const moto3 = { price: 2.00, exclusive: false };
const moto4 = { price: 2.00, exclusive: store1 };
const moto5 = { price: 2.00, exclusive: false };

const findAllMotoboys = () => [moto1, moto2, moto3, moto4, moto5];
const findAllStores = () => [store1, store2, store3];
const findByMotoboy = (motoboy) => findAllMotoboys().filter((moto) => moto === motoboy);
const findByStore = (store) => findAllMotoboys().filter((sto) => sto === store);

const calcDelivery = (moto) => {
    const motoboy = findByMotoboy(moto);
    const reqPrice = store2.requests[0].pedido1;
    const calcDeliveryPrice = reqPrice * 0.05 + motoboy[0].price;

    return { motoboy, store: store2, deliveryPrice: calcDeliveryPrice };
};

console.log(calcDelivery(moto1));