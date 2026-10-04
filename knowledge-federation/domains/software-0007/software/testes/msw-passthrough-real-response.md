---
id: software.testes.tranche15.000864
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/docs/http/handling-requests", "https://mswjs.io/docs/defaults/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: encaminhar requisições com passthrough

## Em uma frase
Retornar `passthrough()` executa a requisição original e devolve a resposta real, e ainda assim a requisição é considerada tratada para fins de resolução.

## Por que importa
Alguns cenários precisam de dados reais de um serviço externo enquanto o restante permanece mockado, e tratar isso como erro ou como handler ausente distorce o resultado.

## Como funciona
Decida dentro do resolver se a requisição vira resposta mockada ou passthrough, e registre a intenção para que a dependência de rede fique explícita na suíte.

## Exemplo
Um handler pode ler o corpo com `request.clone().json()` e devolver `HttpResponse.json()` quando o identificador for conhecido, encaminhando os demais casos com `passthrough()`.

## Limites e trade-offs
Como o passthrough encerra a resolução, handlers posteriores não conseguem mais afetar aquela requisição, o que reduz a capacidade de interceptar o tráfego encaminhado.

## Como verificar
Use uma URL de teste controlada e confirme que a requisição chegou ao serviço real; verifique também que nenhum outro handler tentou tratá-la depois.

## Conexões
- [[msw-handler-order-and-overrides]] — Veja também: MSW: entender ordem e sobreposição de handlers.
- [[msw-httpresponse-construction]] — Veja também: MSW: construir respostas com HttpResponse.

## Fontes
- [MSW — Handling requests](https://mswjs.io/docs/http/handling-requests) — resposta mockada, passthrough e handlers que não respondem; consultado em 2026-10-02.
- [MSW — Default behaviors](https://mswjs.io/docs/defaults/) — fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem; consultado em 2026-10-02.
