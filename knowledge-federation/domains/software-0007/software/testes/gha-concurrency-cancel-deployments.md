---
id: software.testes.tranche08.000224
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

# GitHub Actions: configurar concurrency sem cancelar release válida

## Em uma frase
Use grupos de concurrency com chave que represente o recurso compartilhado e escolha deliberadamente se execução anterior pode ser cancelada.

## Por que importa
Cancelamento indiscriminado pode interromper deploy em andamento, enquanto ausência de controle permite duas execuções mutarem o mesmo ambiente.

## Como funciona
Defina grupo por branch, ambiente ou alvo de deploy conforme exclusão necessária; escolha cancel-in-progress e trate cleanup de job cancelado.

## Exemplo
Builds de uma branch podem substituir execução antiga, mas deploy de produção serializa operações sem cancelar mudança já aplicada parcialmente.

## Limites e trade-offs
Em cada grupo há no máximo uma execução ativa e uma pendente; uma nova execução pode substituir a pendente, portanto não é fila FIFO. Concurrency não substitui lock externo nem garante ordem global entre repositórios.

## Como verificar
Inicie jobs simultâneos e examine qual espera ou cancela; force cancelamento em deploy de teste e confirme estado consistente e recuperável.

## Conexões
- [[gha-environment-protection-gates]] — Veja também: GitHub Actions: verificar gates de environment antes do deploy.
- [[gha-minimum-token-permissions]] — Veja também: GitHub Actions: limitar permissões do token GITHUB_TOKEN.

## Fontes
- [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) — permissions, concurrency, matrices e configuração dos workflows; consultado em 2026-10-02.
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
