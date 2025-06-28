document.addEventListener("DOMContentLoaded", () => {
    const steps = document.querySelectorAll(".step");
    const lines = document.querySelectorAll(".line");

    //steps.forEach((step, index) => {
    //    step.addEventListener("click", () => {
    //        updateSteps(index);
    //    });
  //  });

    function updateSteps(activeIndex) {
        steps.forEach((step, index) => {
            const circle = step.querySelector(".circle");
            const line = lines[index - 1]; // Line is between steps

            if (index <= activeIndex) {
                step.classList.add("active");
                if (line) line.classList.add("active");
            } else {
                step.classList.remove("active");
                if (line) line.classList.remove("active");
            }
        });
    }
});
