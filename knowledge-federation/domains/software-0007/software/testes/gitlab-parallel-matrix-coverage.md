---
id: software.testes.tranche09.000339
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.gitlab.com/ci/yaml/", "https://docs.gitlab.com/ci/jobs/job_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: validar combinações realmente cobertas por parallel matrix

## Em uma frase
parallel matrix expande jobs para combinações configuradas e pode ser limitada por exclusões e dependências.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Matrix que combina versões incompatíveis ou deixa uma plataforma sem job dá falsa impressão de cobertura exaustiva.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Declare dimensões e pares suportados explicitamente e compare jobs materializados com a matriz de compatibilidade do produto.

## Exemplo
Matrix cobre três runtimes e dois bancos em combinações aprovadas sem rodar produto cartesiano de pares sem suporte.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. Variáveis de matrix não provam que runtime foi instalado ou selecionado corretamente dentro da imagem.

## Como verificar
Registre nome e valores de cada job, confira quantidade esperada e valide versão real reportada durante execução.

## Conexões
- [[gitlab-protected-variables-untrusted-pipeline]] — Veja também: GitLab CI: evitar secrets em pipeline não confiável.

## Fontes
- [GitLab CI — YAML syntax reference](https://docs.gitlab.com/ci/yaml/) — semântica de jobs, needs, artifacts e keywords; consultado em 2026-10-02.
- [GitLab CI — Job rules](https://docs.gitlab.com/ci/jobs/job_rules/) — avaliação de rules e prevenção de pipelines duplicados; consultado em 2026-10-02.
