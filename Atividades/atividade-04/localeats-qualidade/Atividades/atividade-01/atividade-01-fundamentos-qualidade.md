# Atividade 1 — Fundamentos e Características da Qualidade no LocalEats

## Tarefa 1: Fundamentos da qualidade

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
| :--- | :--- | :--- | :--- |
| Explícita | Pesquisar ou filtrar restaurantes por especialidade ou localização e visualizar os resultados correspondentes | Usuário final (cliente que busca onde comer) | O usuário não consegue localizar opções adequadas com facilidade e pode abandonar a aplicação |
| Explícita | Realizar um pedido e consultar o histórico/status dos pedidos feitos | Usuário final e restaurante parceiro | O cliente não consegue concluir compras ou acompanhar seus pedidos, gerando perda de pedidos |
| Implícita | Manter o estado de favorito/desfavorito e os dados da conta consistentes entre sessões e recarregamentos | Usuário final | O usuário perde favoritos ou enfrenta comportamentos inconsistentes que reduzem a confiança no sistema |
| Implícita | Responder de forma rápida e previsível durante a navegação, busca e envio de pedidos | Usuário final | A lentidão ou travamentos frustram a experiência e fazem o usuário desistir antes de finalizar o pedido |

Um sistema pode ter todas as funcionalidades solicitadas e ainda apresentar baixa qualidade porque a utilidade funcional não garante boa experiência na prática. Se a busca de restaurantes demorar demais ou perder favoritos entre acessos (necessidades implícitas), o usuário encontrará o recurso na tela, mas enfrentará frustração e insegurança ao usar a aplicação.

## Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
| :--- | :--- | :--- | :--- | :--- |
| Herian | Pesquisar restaurantes por especialidade ou localização | 1. Acessei a aplicação, utilizei o campo de filtro com um termo válido de especialidade/localização e observei a listagem exibida.<br>2. Realizei uma busca com termo inexistente, com uma busca que não existia para verificar o comportamento da tela. | 1. A aplicação exibiu os resultados correspondentes ao termo válido informado na interface.<br>2. A interface apresentou o retorno correspondente ao cenário sem resultados/inválido sem quebrar a página. |  

## Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
| :--- | :--- | :--- | :--- | :--- |
| Herian | Ao pesquisar ou filtrar restaurantes por especialidade ou localização, o LocalEats deve retornar os resultados correspondentes em tempo hábil, sem exibir resultados fora do critério informado nem perder a interatividade da página. | Eficiência de desempenho — Comportamento em relação ao tempo (ISO/IEC 25010) | No LocalEats, a descoberta de restaurantes locais depende diretamente da rapidez com que a busca responde enquanto o usuário navega e compara opções; atrasos longos prejudicam a fluidez da escolha. | Observar e registrar o tempo decorrido entre o envio da pesquisa/filtro e a atualização da lista de restaurantes na tela em diferentes buscas, comparando com a expectativa de resposta imediata do fluxo. |

## Uso de inteligência artificial

**Ferramenta utilizada:**
Assistente de IA generativa.

**Como foi utilizada:**
Apoio na estruturação das tabelas, na redação inicial das necessidades, do requisito de qualidade e das justificativas com base no enunciado da atividade.

**Como as respostas foram verificadas:**
Cada item foi confrontado com as orientações da Atividade 1 e validado conforme a navegação realizada na aplicação LocalEats, garantindo ausência de suposições técnicas não observadas e de dados pessoais.