const canvas = document.getElementById("starCanvas");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

class Star {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.radius = Math.random() * 1.5;
        this.speed = Math.random() * 0.5 + 0.2;
    }
    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI*2);
        ctx.fillStyle = "white";
        ctx.fill();
    }
    update() {
        this.y += this.speed;
        if(this.y > canvas.height){
            this.y = 0;
            this.x = Math.random() * canvas.width;
        }
        this.draw();
    }
}

let stars = [];
for(let i=0;i<100;i++){
    stars.push(new Star());
}

function animateStars(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    stars.forEach(star => star.update());
    requestAnimationFrame(animateStars);
}
animateStars();

window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});