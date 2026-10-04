---
id: software.testes.tranche19.001285
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
fontes: ["https://www.mbtest.org/docs/api/overview", "https://github.com/bbyars/mountebank"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: manter impostores em arquivo

## Em uma frase
A configuração pode ser descrita em arquivo carregado na inicialização, permitindo versionar os serviços virtuais com o projeto.

## Por que importa
O arquivo versionado torna o ambiente de teste reproduzível e revisável, em vez de depender de comandos manuais.

## Como funciona
Mantenha os impostores em arquivo no repositório, nomeie serviços e stubs de forma descritiva e valide a sintaxe antes de subir.

## Exemplo
O arquivo pode descrever os impostores de catálogo, pagamento e notificação usados pela suíte de integração.

## Limites e trade-offs
Arquivos extensos sem organização dificultam revisão, e configurações divergentes entre ambientes geram falhas que só aparecem na esteira.

## Como verificar
Carregue o arquivo em ambiente limpo e confirme que todos os testes que dependem dos impostores passam sem passos manuais.

## Conexões
- [[mountebank-recorded-requests]] — Veja também: Mountebank: inspecionar requisições recebidas.
- [[mountebank-ci-integration]] — Veja também: Mountebank: integrar ao pipeline.

## Fontes
- [Mountebank — API overview](https://www.mbtest.org/docs/api/overview) — interface administrativa, criação de impostores e remoção; consultado em 2026-10-03.
- [Mountebank — repositório oficial](https://github.com/bbyars/mountebank) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
