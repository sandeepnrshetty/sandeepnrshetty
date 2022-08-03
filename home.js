{
    constructor(id, title, description, image)
    {
      this.idCard = id
      this.titre = title
      this.description = description
      this.image = image
    }
    
    initCard()
    {
      this.updateDom();
      this.activateListeners();
    }
    
    updateDom()
    {
      var cardDom = document.getElementById(this.idCard)
      if(cardDom.hasChildNodes()){
        var cardDomImage = cardDom.getElementsByClassName('card-image')[0]
        cardDomImage.src = this.image;
    
        var cardDomTitle = cardDom.getElementsByClassName('card-title')[0]
        cardDomTitle.innerHTML = this.titre;
    
        var cardDomDesc = cardDom.getElementsByClassName('card-desc')[0]
        cardDomDesc.innerHTML = this.description;
      }
    }
    
    activateListeners()
    {
      var cardDom = document.getElementById(this.idCard)
      cardDom.addEventListener("mouseover", function( event ) {
        var cardDomTitle = cardDom.getElementsByClassName('card-title')[0]
        var cardDomDesc = cardDom.getElementsByClassName('card-desc')[0]
        var cardDomMiddle = cardDom.getElementsByClassName('card-mid')[0]
        var cardMiddleHeight = cardDomTitle.offsetHeight + cardDomDesc.offsetHeight;
        cardDomMiddle.style.height = cardMiddleHeight + 15 + "px";
      }, false);
    
      cardDom.addEventListener("mouseout", function( event ) {
        var cardDomMiddle = cardDom.getElementsByClassName('card-mid')[0]
        cardDomMiddle.style.height = 50 + "px";
      }, false);
    }
    }