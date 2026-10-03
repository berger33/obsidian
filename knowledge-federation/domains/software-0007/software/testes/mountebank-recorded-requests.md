---
id: software.testes.tranche19.001284
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.mbtest.org/docs/api/overview", "https://www.mbtest.org/docs/api/stubs"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: inspecionar requisições recebidas

## Em uma frase
Com o registro ativado, o impostor guarda as requisições recebidas e as disponibiliza para consulta posterior.

## Por que importa
O registro transforma o serviço virtual em espião, permitindo verificar o que a aplicação enviou além de simular a resposta.

## Como funciona
Ative o registro no impostor, consulte a lista de requisições ao final do caso e verifique campos relevantes do envio.

## Exemplo
Após um fluxo de cadastro, a consulta pode confirmar que a aplicação enviou o identificador e o formato esperados.

## Limites e trade-offs
Registro desligado esconde o conteúdo enviado, e volumes grandes de requisições dificultam localizar a chamada de interesse.

## Como verificar
Compare a requisição registrada com o contrato esperado e confirme que cabeçalhos e corpo correspondem.

## Conexões
- [[mountebank-injection]] — Veja também: Mountebank: calcular respostas com injeção.
- [[mountebank-file-based-setup]] — Veja também: Mountebank: manter impostores em arquivo.

## Fontes
- [Mountebank — API overview](https://www.mbtest.org/docs/api/overview) — interface administrativa, criação de impostores e remoção; consultado em 2026-10-03.
- [Mountebank — Stubs](https://www.mbtest.org/docs/api/stubs) — stubs, respostas, sequências e stub padrão; consultado em 2026-10-03.
