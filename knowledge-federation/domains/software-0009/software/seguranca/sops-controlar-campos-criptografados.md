---
id: software.seguranca.tranche19.001835
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

# Mozilla SOPS: Controlar campos criptografados

## Em uma frase
**Mozilla SOPS — Controlar campos criptografados:** Seletores de encrypted and unencrypted suffixes ou regex permitem escolher quais valores são cifrados.

## Por que importa
O recorte de **controlar campos criptografados** ajuda a versionar configuração com valores secretos cifrados, mantendo campos públicos legíveis para revisão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **controlar campos criptografados**, SOPS gera ou recupera data key, cifra valores selecionados e cifra essa chave com recipients configurados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Cifre password e token, deixando chaves de configuração sem segredo em uma fixture. Teste em staging autorizado.

## Limites e trade-offs
Suffix ou regex mal configurada pode deixar campo sensível descoberto. Exceções exigem responsável e prazo.

## Como verificar
Varra o plaintext descriptografado e a cópia cifrada para confirmar campos e exceções. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sops-validar-integridade-com-mac]] — Complementa o tópico com mozilla sops: validar integridade com mac.

## Fontes
- [SOPS — Reference](https://getsops.io/docs/reference/) — referência oficial de formatos, cifra de valores e configuração por arquivo; consultado em 2026-10-04.
- [SOPS — Advanced usage](https://getsops.io/docs/usage/advanced/) — guia oficial de creation rules, recipients, rotação e uso avançado; consultado em 2026-10-04.
