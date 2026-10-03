---
id: software.testes.tranche16.001019
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
fontes: ["https://googlechrome.github.io/lighthouse-ci/docs/configuration.html", "https://github.com/GoogleChrome/lighthouse-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Lighthouse CI: escolher destino dos resultados

## Em uma frase
A publicação pode enviar ao armazenamento temporário público, gravar em diretório local ou integrar servidor próprio com histórico.

## Por que importa
O destino determina quem consegue ver o resultado e se medições ficam disponíveis para comparação ao longo do tempo.

## Como funciona
Use armazenamento temporário para compartilhar rapidamente, diretório local para artefato de pipeline e servidor próprio quando o histórico importar.

## Exemplo
Publicar em diretório local permite anexar o relatório ao artefato do trabalho sem expor dados para fora do ambiente.

## Limites e trade-offs
Armazenamento público temporário exige atenção a dados sensíveis e expira após poucos dias, enquanto o servidor próprio adiciona infraestrutura a manter.

## Como verificar
Publique em dois destinos de teste, confirme que os relatórios abrem e verifique se o artefato do pipeline está íntegro.

## Conexões
- [[lighthouseci-performance-budgets]] — Veja também: Lighthouse CI: usar orçamento de desempenho.
- [[lighthouseci-config-file]] — Veja também: Lighthouse CI: versionar a configuração.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
