---
id: software.testes.tranche08.000227
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions", "https://docs.github.com/en/actions/reference/security/secure-use"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitHub Actions: desenhar matrix que detecta incompatibilidade

## Em uma frase
Construa matrix a partir das combinações suportadas e evite expandir uma lista que o produto não promete manter.

## Por que importa
Matrix incompleta deixa regressão de versão escapar; matrix excessiva encarece CI e torna o sinal difícil de interpretar.

## Como funciona
Declare dimensões relevantes, exclusões justificadas e estratégia de fail-fast de acordo com a rapidez de diagnóstico desejada.

## Exemplo
Biblioteca testa versões mínima e máxima suportadas em cada runtime crítico, enquanto combinações oficialmente não suportadas ficam excluídas com motivo.

## Limites e trade-offs
Job verde em matrix não prova todos os ambientes do cliente; runners e imagens também têm diferenças de configuração.

## Como verificar
Gere combinações efetivas e compare com matriz de suporte publicada; provoque falha em uma perna e confira relatório claramente identificável.

## Conexões
- [[gha-path-filters-ci-cobertura]] — Veja também: GitHub Actions: testar path filters e caminhos de validação.
- [[terraform-provider-lockfile-reprodutibilidade]] — Veja também: Terraform: validar reprodutibilidade de providers.

## Fontes
- [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) — permissions, concurrency, matrices e configuração dos workflows; consultado em 2026-10-02.
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
