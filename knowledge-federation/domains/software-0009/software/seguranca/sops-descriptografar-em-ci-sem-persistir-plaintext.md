---
id: software.seguranca.tranche19.001838
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://getsops.io/docs/reference/", "https://getsops.io/docs/usage/advanced/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Mozilla SOPS: Descriptografar em CI sem persistir plaintext

## Em uma frase
**Mozilla SOPS — Descriptografar em CI sem persistir plaintext:** Jobs podem descriptografar durante execução para fornecer configuração a um processo sem versionar o conteúdo claro.

## Por que importa
O recorte de **descriptografar em ci sem persistir plaintext** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **descriptografar em ci sem persistir plaintext**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Monte arquivo temporário em filesystem restrito e remova-o ao término do job. Teste em staging autorizado.

## Limites e trade-offs
Logs de comando, artifacts e cache podem reter segredo fora do arquivo SOPS. Exceções exigem responsável e prazo.

## Como verificar
Verifique permissões, limpeza em sucesso/falha e ausência de plaintext em artefatos do runner. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-gerenciar-key-groups-e-threshold]] — Complementa o tópico com mozilla sops: gerenciar key groups e threshold.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
