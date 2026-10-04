---
id: software.seguranca.tranche19.001831
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

# Mozilla SOPS: Cifrar valores folha do documento

## Em uma frase
**Mozilla SOPS — Cifrar valores folha do documento:** SOPS cifra valores definidos do arquivo e mantém estrutura e partes selecionadas disponíveis para revisão.

## Por que importa
O recorte de **cifrar valores folha do documento** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **cifrar valores folha do documento**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Cifre manifest de teste com um token canário sintético e deixe nomes de campos legíveis para diff. Teste em staging autorizado.

## Limites e trade-offs
Chaves, metadados e campos explicitamente não cifrados podem continuar sensíveis. Exceções exigem responsável e prazo.

## Como verificar
Descriptografe em diretório temporário protegido e confirme quais campos permanecem em claro. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-selecionar-recipients-de-kms]] — Complementa o tópico com mozilla sops: selecionar recipients de kms.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
