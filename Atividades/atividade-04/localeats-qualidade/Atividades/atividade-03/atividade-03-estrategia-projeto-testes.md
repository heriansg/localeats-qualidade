# Atividade 3 — Estratégia e Projeto de Testes do LocalEats

## Tarefa 1: Planejamento dos testes

### 1.1 Objetivo dos testes
Verificar se os fluxos selecionados do LocalEats funcionam conforme as regras esperadas — incluindo autenticação de acesso e realização de pedidos — prevenindo falhas críticas antes da disponibilização da aplicação.

### 1.2 Escopo

| Integrante | Funcionalidade incluída | O que será verificado |
| :--- | :--- | :--- |
| Herian | Entrar no sistema | Validação de credenciais válidas e inválidas, feedback ao usuário e acesso à área autenticada |

| Funcionalidade não incluída | Justificativa |
| :--- | :--- |
| Favoritar e desfavoritar restaurantes | Não faz parte do recorte principal escolhido para esta etapa de planejamento de testes |

### 1.3 Abordagem

| Item | Decisão da equipe | Justificativa |
| :--- | :--- | :--- |
| Níveis de teste | Teste de sistema | Avalia o fluxo de entrada no sistema pela interface da aplicação publicada de ponta a ponta |
| Tipos de teste | Teste funcional | Foca no comportamento esperado das regras de login e mensagens exibidas ao usuário |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Os testes são projetados a partir das entradas e respostas observáveis na interface, sem depender do código interno |
| Técnicas de teste | Tabela de decisão e particionamento de equivalência | A autenticação depende de combinações de condições (usuário e senha) e de classes de entradas válidas e inválidas |

### 1.4 Ambiente e responsabilidades

| Item | Definição |
| :--- | :--- |
| Ambiente necessário | Aplicação acessível em `https://local-eats-unisenac.vercel.app/`, navegador web atualizado em desktop ou dispositivo móvel, conexão estável com a internet e conta de teste não sensível (sem senha pessoal real) |
| Responsáveis pelo planejamento | [Seu Nome Completo] |
| Responsáveis pela especificação dos casos | [Seu Nome Completo] |
| Responsáveis pela futura execução | [Seu Nome Completo] |

### 1.5 Critérios

| Critério | Definição da equipe |
| :--- | :--- |
| Entrada | Aplicação `https://local-eats-unisenac.vercel.app/` acessível no navegador e dados de teste válidos/inválidos definidos |
| Saída | Todos os casos de teste especificados revisados e rastreados aos riscos e técnicas correspondentes |
| Suspensão | Aplicação fora do ar / inacessível ou indisponibilidade da tela de entrada no sistema |

## Tarefa 2: Riscos e técnicas de teste

### 2.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R01 | Herian| Entrar no sistema | Usuário com credenciais inválidas ou campos vazios conseguir acessar a conta ou não receber mensagem clara de erro | Acesso indevido ou confusão do usuário sem saber por que o login falhou, prejudicando o uso do LocalEats | Média | Alto | Alta | A falha de autenticação compromete a segurança do acesso ou bloqueia usuários legítimos logo na entrada |
| R02 | Herian | Entrar no sistema | Usuário com credenciais válidas não conseguir entrar no sistema após submeter o formulário | O cliente fica impedido de acessar sua conta, favoritar restaurantes e fazer ou consultar pedidos | Média | Alto | Alta | Impede o acesso a funcionalidades centrais da aplicação após a tela inicial |

### 2.2 Aplicação da técnica

**Integrante responsável**
Nome: Herian
Funcionalidade: Entrar no sistema
Risco relacionado: R01 e R02
Técnica escolhida: Tabela de decisão (complementada por particionamento de equivalência para campos vazios/inválidos)

**Por que a técnica foi escolhida?**
O resultado do login depende diretamente da combinação entre a validade do identificador de acesso (e-mail/usuário) e da senha informada, tornando a tabela de decisão clara e objetiva para cobrir todas as combinações relevantes.

**Aplicação da técnica**

| Regra | Usuário/e-mail válido e preenchido? | Senha válida e preenchida? | Resultado esperado |
| :---: | :---: | :---: | :--- |
| 1 | Sim | Sim | Permitir entrada no sistema e direcionar para a sessão autenticada |
| 2 | Sim | Não (vazia ou incorreta) | Bloquear o acesso e exibir mensagem de erro/validação |
| 3 | Não (vazio ou inválido) | Sim | Bloquear o acesso e exibir mensagem de erro/validação |
| 4 | Não | Não | Bloquear o acesso e informar obrigatoriedade/invalidade dos campos |

**Casos derivados**
CT01, CT02 e CT03

## Tarefa 3: Casos de teste e rastreabilidade

### 3.1 Especificação dos casos de teste

**CT01: Login bem-sucedido com credenciais válidas**
Integrante responsável: [Seu Nome Completo]
Funcionalidade: Entrar no sistema
Risco ou requisito relacionado: R02
Técnica utilizada: Tabela de decisão (Regra 1)
Pré-condição:
A aplicação está aberta em `https://local-eats-unisenac.vercel.app/` e existe uma conta de teste válida cadastrada.
Dados de entrada:
E-mail/usuário de teste válido e senha válida da conta de teste.
Passos:
1. Acessar a opção de entrar no sistema.
2. Preencher os campos de acesso com as credenciais válidas.
3. Confirmar/enviar o formulário de login.
Resultado esperado:
O usuário entra no sistema com sucesso e a interface reflete a sessão autenticada.

**CT02: Bloqueio de login com senha incorreta**
Integrante responsável: Herian
Funcionalidade: Entrar no sistema
Risco ou requisito relacionado: R01
Técnica utilizada: Tabela de decisão (Regra 2)
Pré-condição:
A aplicação está aberta na tela de entrar no sistema e o usuário de teste existe.
Dados de entrada:
E-mail/usuário de teste válido e uma senha incorreta.
Passos:
1. Informar o e-mail/usuário válido no campo correspondente.
2. Informar uma senha incorreta no campo de senha.
3. Acionar o botão de entrar.
Resultado esperado:
O acesso é bloqueado e o sistema exibe uma mensagem indicando credenciais inválidas ou falha no login.

**CT03: Bloqueio de login com campos obrigatórios vazios**
Integrante responsável: Herian
Funcionalidade: Entrar no sistema
Risco ou requisito relacionado: R01
Técnica utilizada: Tabela de decisão (Regra 4) e particionamento de equivalência (classe inválida de campo vazio)
Pré-condição:
A aplicação está aberta na tela de entrar no sistema.
Dados de entrada:
Campos de e-mail/usuário e senha deixados em branco.
Passos:
1. Acessar a tela de entrar no sistema sem preencher e-mail/usuário nem senha.
2. Tentar enviar o formulário de login.
Resultado esperado:
O login não é realizado e a aplicação impede o envio ou exibe aviso de preenchimento obrigatório.

### 3.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
| :--- | :--- | :--- | :--- | :--- |
| Herian| Entrar no sistema | R01: acesso indevido ou ausência de feedback em credenciais inválidas/vazias | Tabela de decisão e particionamento de equivalência | CT02 e CT03 |
| Herian | Entrar no sistema | R02: falha ao autenticar com credenciais válidas | Tabela de decisão | CT01 |

## Uso de inteligência artificial

**Ferramenta utilizada:**
Assistente de IA generativa.

**Como foi utilizada:**
Apoio na estruturação do plano de testes, sugestão de riscos e casos de teste para a funcionalidade de entrar no sistema e organização da matriz de rastreabilidade.

**Uma sugestão que precisou ser alterada ou rejeitada:**
Ajuste dos cenários para manter aderência estrita às funcionalidades descritas do LocalEats e evitar inclusão de resultado obtido ou evidências de execução (já que a Atividade 3 foca no planejamento e projeto sem execução nesta etapa).

**Como as respostas foram verificadas:**
Revisão completa de cada tabela, risco, técnica, caso de teste e linha da matriz de rastreabilidade em relação ao enunciado da Atividade 3 e ao funcionamento do LocalEats.