<script>
    document.addEventListener('DOMContentLoaded', function() {
        console.log('Script carregado e DOM pronto.');
        document.querySelectorAll('.btn-update-cart').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            console.log("botão de atualizar clicado")
            const itemId = this.getAttribute('data-id');
            const quantityInput = document.getElementById(`quantity-${itemId}`);
            const quantity = quantityInput.value;

            if (!quantity) {
                alert('Por favor, insira a quantidade.');
                return;
            }

            const url = new URL(this.href, window.location.origin);
            url.searchParams.set('quantity', quantity);
            console.log(url.toString());
            window.location.href = url;
        });
        });
    });
</script>