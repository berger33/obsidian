---
id: software.testes.tranche09.000338
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
fontes: ["https://docs.gitlab.com/ci/variables/", "https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: evitar secrets em pipeline não confiável

## Em uma frase
Variáveis protegidas e permissões de pipeline podem restringir exposição de credenciais, mas fork/MR e configurações do projeto exigem verificação explícita.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Job de validação de código externo não deve receber token de deploy nem acesso privilegiado por acidente.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Separe testes sem segredo de jobs de release protegidos e aplique escopo e ambientes aprovados às credenciais sensíveis.

## Exemplo
MR de fork executa lint e testes isolados; deploy que usa segredo só roda após aprovação e branch protegida.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. Mascaramento em log não impede exfiltração por script malicioso com acesso à variável.

## Como verificar
Teste pipeline em fork de laboratório, inspecione env disponíveis e confirme que código não confiável não consegue iniciar job privilegiado.

## Conexões
- [[gitlab-rules-changes-path-coverage]] — Veja também: GitLab CI: testar path rules para não pular validação compartilhada.
- [[gitlab-parallel-matrix-coverage]] — Veja também: GitLab CI: validar combinações realmente cobertas por parallel matrix.

## Fontes
- [GitLab CI — Variables](https://docs.gitlab.com/ci/variables/) — escopo, proteção e exposição de variáveis CI/CD; consultado em 2026-10-02.
- [GitLab CI — Merge request pipelines](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/) — condições e configuração de merge request pipelines; consultado em 2026-10-02.
