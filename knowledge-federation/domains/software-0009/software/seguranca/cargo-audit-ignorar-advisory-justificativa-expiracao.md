---
id: software.seguranca.tranche17.001605
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md", "https://rustsec.org/advisories/RUSTSEC-2017-0001.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ignorar um advisory em `cargo-audit`: exceção rastreável, justificativa e reavaliação

## Em uma frase
`--ignore` e a configuração `audit.toml` permitem silenciar um advisory específico, mas a exceção deve explicar por que o achado não se aplica ao produto.

## Por que importa
Ignorar por conveniência pode esconder uma correção futura ou uma mudança de feature; a justificativa torna explícito o pressuposto técnico para quem revisará o código depois.

## Como funciona
Priorize atualização; se indisponível, documente o caminho de código não usado, versão analisada, responsável e data de revisão, e mantenha a exceção pequena e verificável.

## Exemplo
Em vez de suprimir a categoria inteira, registre somente o ID confirmado no relatório e anexe evidência de que a API afetada não é chamada nesta configuração.

```text
cargo audit --ignore RUSTSEC-2017-0001
```

## Limites e trade-offs
A exceção não corrige a crate, não demonstra ausência de risco em builds alternativos e pode ficar obsoleta quando features ou dependências mudarem.

## Como verificar
Faça um teste de CI que falhe quando a exceção desaparecer ou ficar sem justificativa, e reavalie o advisory após atualização de versão ou configuração.

## Conexões
- [[cargo-audit-opcao-file-lockfile-externo-reproducibilidade]] — `cargo audit --file`: auditar um `Cargo.lock` externo sem entrar no workspace.
- [[cargo-audit-config-audittoml-controle-versao-excecoes]] — `audit.toml` versionado: governança das exceções locais do `cargo-audit`.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — opções `--ignore` e `audit.toml` para advisories específicos; consultado em 2026-10-04.
- [RustSec Advisory Database — Advisory RUSTSEC-2017-0001](https://rustsec.org/advisories/RUSTSEC-2017-0001.html) — exemplo publicado e verificável de um ID RUSTSEC real usado na linha de comando; consultado em 2026-10-04.
