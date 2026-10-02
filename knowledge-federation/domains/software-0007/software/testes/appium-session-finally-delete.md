---
id: software.testes.tranche11.000544
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://appium.io/docs/en/latest/quickstart/test-js/", "https://appium.io/docs/en/latest/guides/caps/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: encerrar session em finally após cada fluxo

## Em uma frase
Quickstart abre session remota e chama deleteSession ao concluir interação; lifecycle da sessão é responsabilidade do cliente de teste.

## Por que importa
Falha antes do encerramento pode deixar device ocupado, app em estado inesperado e próximo teste associado a sessão antiga.

## Como funciona
Guarde driver em escopo de teste e finalize sessão em bloco de cleanup que rode também quando comando/assertion lança erro.

## Exemplo
Teste navega settings e encerra sessão em finally; caminho de assertion falha ainda executa deleteSession.

## Limites e trade-offs
Pausa fixa para visualização não substitui condição de espera e pode alongar suite sem garantir prontidão.

## Como verificar
Injete exceção no meio do teste e confirme que sessão some do servidor e device fica disponível.

## Conexões
- [[appium-context-native-webview]] — Veja também: Appium: consultar contexts antes de alternar entre native e webview.
- [[appium-w3c-actions-vs-comandos-driver]] — Veja também: Appium: separar W3C Actions de comandos móveis específicos.

## Fontes
- [Appium — Write a Test (JS)](https://appium.io/docs/en/latest/quickstart/test-js/) — criação e término de sessão por cliente e capabilities de exemplo; consultado em 2026-10-02.
- [Appium — Session Capabilities](https://appium.io/docs/en/latest/guides/caps/) — parâmetros W3C de criação de sessão, prefixos Appium e capabilities imutáveis; consultado em 2026-10-02.
