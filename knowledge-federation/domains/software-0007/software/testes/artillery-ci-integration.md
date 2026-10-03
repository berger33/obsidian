---
id: software.testes.tranche16.000971
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://www.artillery.io/docs/get-started/first-test", "https://github.com/artilleryio/artillery"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: integrar a carga ao pipeline

## Em uma frase
A execução pode gravar o resumo em arquivo e devolver código de erro pelos limites, permitindo que a verificação de desempenho participe do fluxo automático.

## Por que importa
Um teste de carga rodado apenas manualmente envelhece sem referência comparável, enquanto o registro versionado permite acompanhar tendência entre revisões.

## Como funciona
Grave o resultado em arquivo, publique-o como artefato e execute a verificação contra um ambiente estável com dados representativos.

## Exemplo
Guardar o resumo de cada execução permite comparar percentuais de latência entre a versão atual e a anterior antes de promover a mudança.

## Limites e trade-offs
Medições contra ambientes compartilhados sofrem interferência de outros testes e de dados variáveis, o que exige janela controlada e interpretação cautelosa.

## Como verificar
Rode a verificação em duas revisões consecutivas e confirme que os artefatos permitem comparar as duas medições de forma direta.

## Conexões
- [[artillery-rate-vs-concurrency]] — Veja também: Artillery: compreender o modelo de geração de carga.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
