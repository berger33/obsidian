---
id: software.testes.tranche14.000818
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
fontes: ["https://tox.wiki/en/latest/how-to/usage.html", "https://tox.wiki/en/latest/reference/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# tox: dar basetemp distinto a cada pytest paralelo

## Em uma frase
Quando tox paraleliza ambientes que executam pytest, cada invocação deve usar diretório temporário próprio para evitar colisões.

## Por que importa
Fixtures que escrevem nomes iguais podem falhar intermitentemente apenas quando versões da matriz rodam juntas.

## Como funciona
Passe `--basetemp` apontando para diretório exclusivo do ambiente, como o placeholder de diretório temporário que tox fornece.

## Exemplo
Dois ambientes Python criam arquivos homônimos sem compartilhar a mesma raiz temporária, mantendo comparação de resultados confiável.

## Limites e trade-offs
Diretório único corrige apenas a colisão de filesystem; bancos, portas e serviços externos continuam exigindo isolamento separado.

## Como verificar
Repita modo paralelo com execução de testes que grava arquivos e verifique limpeza e exclusividade dos diretórios.

## Conexões
- [[tox-exec-is-not-configured-test-run]] — Veja também: tox: usar exec para ferramenta sem executar os hooks do ambiente.
- [[tox-package-under-test-contract]] — Veja também: tox: verificar o artefato instalado e não só o checkout.

## Fontes
- [tox — How-to usage](https://tox.wiki/en/latest/how-to/usage.html) — execução sequencial/paralela, seleção por ambiente, logs e diretórios temporários; consultado em 2026-10-02.
- [tox — Configuration reference](https://tox.wiki/en/latest/reference/config.html) — lista de ambientes, fatores, TOML, templates e configurações por ambiente; consultado em 2026-10-02.
