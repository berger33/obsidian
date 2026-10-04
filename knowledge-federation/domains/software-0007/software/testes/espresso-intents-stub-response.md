---
id: software.testes.tranche14.000794
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://developer.android.com/training/testing/espresso/intents", "https://developer.android.com/training/testing/espresso"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso-Intents: simular resposta externa com intending

## Em uma frase
`intending()` configura uma resposta para intents de saída correspondentes e permite testar o fluxo local sem abrir o aplicativo externo.

## Por que importa
O stub torna determinístico um boundary que depende de navegador, seletor de arquivo ou outra atividade do sistema.

## Como funciona
Registre matcher e resultado antes de executar a ação; depois verifique que a aplicação processou o retorno esperado.

## Exemplo
Um teste de compartilhamento pode combinar `intending(matcher).respondWith(result)` com uma assertion na UI depois que o app recebe o resultado.

## Limites e trade-offs
O stub testa o contrato que a aplicação envia e a resposta configurada, não a integração real com o destino.

## Como verificar
Compare matcher do stub e intent enviado, e preserve um teste de dispositivo quando a integração de sistema for requisito.

## Conexões
- [[espresso-intents-validate-outgoing]] — Veja também: Espresso-Intents: validar o intent que o app tentou enviar.
- [[espresso-adapter-view-ondata-selection]] — Veja também: Espresso: localizar item de AdapterView com onData.

## Fontes
- [Android — Espresso-Intents](https://developer.android.com/training/testing/espresso/intents) — correspondência, verificação e stubbing de intents de saída; consultado em 2026-10-02.
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
