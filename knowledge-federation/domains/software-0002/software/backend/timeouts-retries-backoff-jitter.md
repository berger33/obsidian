---
id: software.backend.retries-resilientes.000001
tipo: tecnica
dominio: software
subdominio: backend
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/", "https://sre.google/sre-book/handling-overload/"]
tags: [dominio/software, subdominio/backend, qualidade/candidata]
aliases: [Timeouts, retries, backoff e jitter]
---

# Timeouts, retries, backoff e jitter

## Em uma frase
Um retry controlado pode absorver falhas transitórias; timeout, backoff, jitter e orçamento de tentativas limitam o custo e impedem que a recuperação aumente a sobrecarga.

## Por que importa
Uma chamada remota pode falhar por perda de pacote, reinício ou saturação temporária. Sem timeout, a requisição pode consumir conexões e threads indefinidamente. Sem limite de tentativas, uma dependência lenta recebe ainda mais tráfego justamente quando tem menos capacidade. Esse ciclo transforma uma falha parcial em indisponibilidade maior.

## Como funciona
Defina um deadline total para a operação e derive dele o tempo máximo de cada tentativa. Repita somente erros classificados como transitórios e operações repetíveis com segurança. Use backoff exponencial limitado para espaçar tentativas; some jitter aleatório para que clientes diferentes não sincronizem novos picos. Limite o número total de tentativas e, para sistemas de alto tráfego, reserve um orçamento de retries por cliente ou serviço. Evite retries em várias camadas: se cada uma de três camadas fizer até três chamadas totais (incluindo a inicial), uma chamada lógica pode resultar em até 27 chamadas a jusante. Declare explicitamente se o orçamento conta a tentativa inicial.

## Exemplo
Uma API com deadline de dois segundos tenta uma dependência até três vezes. Cada espera cresce, tem teto e jitter, mas nunca ultrapassa o deadline restante. Um erro de validação não é repetido; um timeout pode ser repetido se a operação for idempotente. Se o orçamento local acabou, o serviço falha rapidamente e expõe o erro ao chamador.

## Limites e trade-offs
Backoff não corrige uma falha permanente nem aumenta a capacidade do serviço. Um timeout baixo demais causa falsos erros; alto demais ocupa recursos. Circuit breakers podem ajudar em alguns contextos, mas introduzem estado e modos adicionais que precisam ser testados. A política correta depende de latência, semântica da operação e sinais da dependência.

## Como verificar
Teste atrasos, desconexão antes e depois da gravação, respostas 429/5xx, deadline esgotado e orçamento de retry consumido. Meça tentativas por chamada lógica, tráfego de retry e latência final. Verifique que o sistema reduz tentativas sob sobrecarga e que apenas uma camada é responsável por repetir.

## Conexões
- [[idempotencia-http-api]] — pré-condição importante para repetir mutações com segurança.
- [[observabilidade-sinais-distribuidos]] — torna visíveis tentativas e latências por dependência.
- [[sli-slo-orcamento-de-erro]] — conecta política de retry ao impacto percebido pelo usuário.

## Fontes
- [AWS Builders’ Library — Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — decisões sobre timeouts, retries limitados e jitter; acesso em 2026-10-01.
- [Google SRE Book — Handling Overload](https://sre.google/sre-book/handling-overload/) — retry budgets e contenção de amplificação de carga; acesso em 2026-10-01.
