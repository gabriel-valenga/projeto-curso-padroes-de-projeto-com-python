function deletarProduto(id) {
    if (!confirm(`Tem certeza que deseja deletar o produto ${id}?`)) {
      return;
    }
  
    fetch(`/produto/delete/${id}`, {
      method: 'DELETE',
    })
    .then(response => {
      if (response.redirected) {
        window.location.href = response.url;
      } else if (response.ok) {
        alert('Produto deletado com sucesso!');
      } else {
        alert('Erro ao deletar produto.');
      }
    })
    .catch(error => {
      console.error('Erro na requisição:', error);
    });
  }
  