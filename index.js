function hideAllSteps() {
    const steps = document.querySelectorAll('.step');
    steps.forEach(step => step.style.display = 'none');
  }
  
  function showStartHere() {
    hideAllSteps();
    document.getElementById('start-here').style.display = 'block';
    document.getElementById('insurance-career').style.display = 'none';
    document.getElementById('cost-estimates').style.display = 'none';
  }
  
  function showInsuranceCareer() {
    hideAllSteps();
    document.getElementById('insurance-career').style.display = 'block';
  }
  
  function showCostEstimates() {
    hideAllSteps();
    document.getElementById('cost-estimates').style.display = 'block';
  }
  
  // Initially show the Start Here step
  showStartHere();