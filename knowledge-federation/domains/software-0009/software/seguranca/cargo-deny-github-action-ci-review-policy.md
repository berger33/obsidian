---
id: software.seguranca.tranche17.001620
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://github.com/EmbarkStudios/cargo-deny-action", "https://embarkstudios.github.io/cargo-deny/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Executar `cargo-deny` em CI: configuração como código e feedback de pull request

## Em uma frase
A documentação do projeto mostra `cargo deny check` como comando principal e apresenta uma action de CI para executar as regras em pushes e pull requests.

## Por que importa
Executar as mesmas regras a cada mudança reduz diferenças entre laptops e integração contínua e mostra o impacto de atualizar dependências antes do merge.

## Como funciona
Fixe versões da ferramenta e da action, faça upload do relatório e permita que exceções sejam revisadas como diffs comuns do arquivo de policy.

## Exemplo
Um workflow pode executar `cargo deny check` após checkout e falhar a verificação quando uma alteração introduz licença, source ou advisory não aceito.

```text
cargo deny check
```

## Limites e trade-offs
A action aplica a configuração presente no repositório; se a policy estiver incompleta ou desatualizada, a automação apenas repetirá a lacuna.

## Como verificar
Teste deliberadamente uma dependência recusada em branch temporária e confirme status não verde, relatório legível e caminho documentado de remediação.

## Conexões
- [[cargo-deny-target-features-grafo-resolucao-reprodutivel]] — Alvos e features na policy do `cargo-deny`: auditar o grafo que realmente será compilado.

## Fontes
- [`cargo-deny` — GitHub Action oficial](https://github.com/EmbarkStudios/cargo-deny-action) — inputs, comandos, matriz de checks e comportamento de falha da action; consultado em 2026-10-04.
- [`cargo-deny` — documentação oficial](https://embarkstudios.github.io/cargo-deny/) — execução de `cargo deny check` sobre a configuração do projeto; consultado em 2026-10-04.
