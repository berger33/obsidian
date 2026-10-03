---
id: software.testes.tranche16.000958
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
fontes: ["https://wix.github.io/Detox/docs/introduction/getting-started", "https://wix.github.io/Detox/docs/introduction/project-setup"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Detox: preservar artefatos das falhas

## Em uma frase
A execução pode capturar telas e gravar vídeos nos casos que falham, produzindo evidência sem exigir reprodução local do problema.

## Por que importa
Falhas em integração contínua são difíceis de investigar quando não há imagem nem gravação do momento exato em que a asserção não se confirmou.

## Como funciona
Ative a captura apenas em falhas para controlar volume, escolha um diretório de artefatos no pipeline e complemente com capturas nomeadas em marcos do fluxo.

## Exemplo
Uma captura nomeada logo após o login documenta o estado esperado e ajuda a comparar com a imagem automática gerada quando a etapa seguinte falha.

## Limites e trade-offs
Vídeos e imagens podem conter dados pessoais e crescer rapidamente; a política de retenção precisa ser definida antes de publicar o artefato.

## Como verificar
Provoque uma falha controlada, confirme quais arquivos foram gerados e verifique se o artefato do pipeline contém a evidência do caso.

## Conexões
- [[detox-device-actions]] — Veja também: Detox: usar ações de dispositivo no fluxo.
- [[detox-configuration-file]] — Veja também: Detox: descrever alvos no arquivo de configuração.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — Project Setup](https://wix.github.io/Detox/docs/introduction/project-setup) — configuração por alvo, arquivo de configuração e comandos de build e teste; consultado em 2026-10-03.
