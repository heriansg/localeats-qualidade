# Atividade 2 — Organização da Qualidade no LocalEats

## Tarefa 1: Diagnóstico da situação

| Problema identificado | Possível consequência para o produto ou para a equipe |
| :--- | :--- |
| Critérios para considerar uma funcionalidade pronta ("pronto") não estão claros e não há aprovação formal de versão | Funcionalidades com problemas chegam aos usuários e geram incerteza sobre quem responde pela liberação de novas versões |
| Crença de que apenas o QA é responsável por testar | Sobrecarga no papel de QA, detecção tardia de defeitos e código chegando ao teste sem verificação prévia pelo desenvolvimento |
| Defeitos encontrados nem sempre são registrados ou acompanhados | Falhas recorrem em novas entregas, perda de histórico de problemas e retrabalho sem rastreabilidade |

A qualidade do LocalEats não deve ser responsabilidade exclusiva do QA porque a qualidade é construída em cada etapa do desenvolvimento. Se apenas o QA testar no fim, falhas de regra de negócio, código ou critérios mal definidos surgem tarde e encarecem a correção.

## Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
| :--- | :--- | :--- | :--- | :--- |
| Herian | QA ou analista de qualidade | Apoiar a definição de critérios de aceitação, planejar e executar testes do sistema, registrar/acompanhar defeitos e apoiar a verificação para liberação | Conhecimento de técnicas de teste (caixa-preta, limites, equivalência, decisão/estados), elaboração de casos de teste e registro estruturado de defeitos | Comunicação clara, pensamento crítico, colaboração com o time e foco na prevenção de problemas |
| Herian| Responsável pelo produto (PO) | Definir requisitos e critérios de aceitação claros e priorizar a correção de defeitos conforme impacto ao usuário e ao negócio | Levantamento e especificação de requisitos funcionais e regras de negócio, priorização de backlog e análise de impacto | Tomada de decisão, negociação, empatia com o usuário e clareza na comunicação |
| Herian | Desenvolvedor | Implementar funcionalidades, revisar código, criar testes unitários e corrigir defeitos identificados | Domínio da stack do projeto, escrita de testes unitários, leitura de logs/erros e uso de controle de versão | Atenção a detalhes, abertura a feedback, trabalho em equipe e corresponsabilidade pela qualidade |
| Herian | Liderança técnica | Apoiar revisões técnicas de requisitos e código, alinhar padrões de qualidade e apoiar decisões de liberação | Arquitetura da aplicação, revisão de código, boas práticas de engenharia e diagnóstico de falhas técnicas | Liderança colaborativa, visão sistêmica, mediação de conflitos e responsabilidade técnica |

## Tarefa 3: Matriz de responsabilidades

| Atividade de qualidade | Responsável pelo produto | Desenvolvedor | QA ou analista de qualidade | Liderança técnica |
| :--- | :---: | :---: | :---: | :---: |
| Definir critérios de aceitação | A / R | C | C | C |
| Revisar requisitos | A | C | R | C |
| Implementar a funcionalidade | I | R | I | C |
| Revisar o código | I | R | I | A |
| Criar testes unitários | I | R | C | C |
| Planejar e executar testes do sistema | I | C | A / R | I |
| Registrar e acompanhar defeitos | I | C | A / R | I |
| Priorizar a correção dos defeitos | A / R | C | C | C |
| Aprovar a disponibilização da versão | A | I | R | C |

### Lacuna ou conflito encontrado
Na atividade **Aprovar a disponibilização da versão**, o QA aparece como **R** (executa a verificação de prontidão/critérios) e o Responsável pelo produto como **A** (aprova a entrega), mas sem um *checklist* formal de "pronto para release" a decisão pode gerar atrito quando houver defeitos menores abertos. Além disso, o acompanhamento contínuo de defeitos pode ficar concentrado no QA se os desenvolvedores não atualizarem o status ao corrigir.

### Práticas recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
| :--- | :--- | :--- |
| Critérios de aceite e *Definition of Done* (DoD) explícitos antes de iniciar a implementação | Falta de clareza sobre quando uma funcionalidade está pronta e defeitos chegando aos usuários | Responsável pelo produto, QA ou analista de qualidade, Desenvolvedor e Liderança técnica |
| Fluxo padrão de registro e triagem periódica de defeitos com critérios de liberação | Defeitos não registrados ou acompanhados e indefinição sobre a aprovação de novas versões | QA ou analista de qualidade, Responsável pelo produto, Desenvolvedor e Liderança técnica |

## Uso de inteligência artificial

**Ferramenta utilizada:**
Assistente de IA generativa.

**Como foi utilizada:**
Apoio para organizar o diagnóstico dos problemas, estruturar a tabela de papéis e competências, montar a matriz RACI e redigir a lacuna e as práticas recomendadas.

**Como as respostas foram verificadas:**
Revisão manual de todas as linhas da matriz RACI para garantir que cada atividade tivesse ao menos um `R` e exatamente um `A`, além da conferência com o contexto do LocalEats e as regras da Atividade 2.