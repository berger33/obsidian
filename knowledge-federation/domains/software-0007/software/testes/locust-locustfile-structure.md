---
id: software.testes.tranche17.001066
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://github.com/locustio/locust"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: escrever o arquivo de teste

## Em uma frase
O arquivo descreve classes de usuário com tarefas anotadas, e a ferramenta gera a carga executando essas tarefas em processos distribuídos.

## Por que importa
Carga descrita em código Python permite reutilizar bibliotecas do projeto, tratar respostas e variar o comportamento por ambiente.

## Como funciona
Defina uma classe de usuário, declare o tempo de espera e marque as tarefas, informando o endereço alvo por linha de comando.

## Exemplo
Um arquivo pode definir classes distintas para visitante e administrador, escolhidas no momento da execução pela linha de comando.

## Limites e trade-offs
Múltiplas classes no mesmo arquivo exigem escolha explícita na execução, e tarefas que dependem de módulos pesados atrasam a inicialização de cada processo.

## Como verificar
Execute o arquivo com poucos usuários em ambiente controlado e confirme que o resumo lista as tarefas e as requisições esperadas.

## Conexões
- [[locust-tasks-and-weights]] — Veja também: Locust: ponderar tarefas do usuário.

## Fontes
- [Locust — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida; consultado em 2026-10-03.
- [Locust — repositório oficial](https://github.com/locustio/locust) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
