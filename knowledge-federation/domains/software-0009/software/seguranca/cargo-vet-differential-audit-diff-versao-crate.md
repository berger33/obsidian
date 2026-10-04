---
id: software.seguranca.tranche17.001625
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
fontes: ["https://mozilla.github.io/cargo-vet/performing-audits.html", "https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-diff"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria diferencial no `cargo-vet`: revisar a diferença entre versões de uma crate

## Em uma frase
Quando já existe uma auditoria para outra versão, o cargo-vet pode calcular a diferença relevante e guiar a revisão do código que mudou.

## Por que importa
Revisar apenas o delta reduz esforço sem tratar uma atualização como idêntica à versão previamente auditada.

## Como funciona
Use `inspect` e `diff` para obter fontes e comparar a versão nova com a base registrada, mantendo evidência do que foi examinado.

## Exemplo
Ao atualizar uma crate, revise o diff sugerido, identifique arquivos de código e mudanças de build e registre uma nova auditoria para a versão resolvida.

```text
cargo vet diff
```

## Limites e trade-offs
A diferença só é tão confiável quanto a base e a seleção de arquivos; uma auditoria anterior não cobre automaticamente mudanças posteriores.

## Como verificar
Confirme no registro qual versão antiga serviu de base, abra o diff gerado e compare seu resultado com o pacote efetivamente selecionado no lockfile.

## Conexões
- [[cargo-vet-criteria-safe-to-run-safe-to-deploy]] — Critérios do `cargo-vet`: definir o que uma auditoria precisa demonstrar.
- [[cargo-vet-imports-organizacoes-trust-explicito]] — Imports de auditorias no `cargo-vet`: confiar em organizações de forma explícita.

## Fontes
- [Cargo Vet — Performing Audits](https://mozilla.github.io/cargo-vet/performing-audits.html) — escolha de diff diferencial, inspeção de versões e sugestão de menor esforço; consultado em 2026-10-04.
- [Cargo Vet — Commands: diff/inspect](https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-diff) — sintaxe e saída dos subcomandos de inspeção/diff; consultado em 2026-10-04.
