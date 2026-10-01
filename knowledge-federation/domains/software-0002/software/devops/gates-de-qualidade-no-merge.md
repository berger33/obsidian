---
id: software.devops.gates-merge.000001
tipo: pratica
dominio: software
subdominio: devops
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: pendente
revisor: ""
fontes: ["https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches", "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
aliases: [Quality gates, Proteção de branch e checks]
---

# Gates de qualidade antes do merge

## Em uma frase
Gates de merge são verificações explícitas que precisam passar antes de integrar uma mudança; eles tornam requisitos repetíveis, mas não substituem revisão técnica nem bons testes.

## Por que importa
Sem critérios claros, qualidade depende de memória e disciplina individual. Um pipeline automatizado pode impedir que testes conhecidos falhem silenciosamente, que contratos quebrem consumidores ou que uma migração fora do padrão chegue à branch protegida. O gate precisa ser relevante para o risco e oferecer um resultado compreensível para quem corrige a mudança.

## Como funciona
Uma política pode exigir pull request, aprovação, resolução de conversas e status checks bem definidos. Em CI, os checks podem executar formatação, análise estática, testes unitários e de contrato, verificações de dependências e validação de documentação. A configuração do branch liga nomes de checks a critérios de integração. Jobs obrigatórios devem ter nomes únicos e resultados previsíveis; um check ignorado por filtro de paths pode permanecer pendente e bloquear a integração, dependendo da configuração.

## Exemplo
Uma alteração em um endpoint executa testes unitários, valida o documento OpenAPI e verifica contratos publicados. Uma mudança de schema dispara testes de migração. Um resultado verde autoriza a etapa seguinte, mas a revisão humana ainda avalia intenção, compatibilidade, segurança e impacto operacional que os testes não cobrem.

## Limites e trade-offs
Mais gates elevam confiança apenas quando os checks são confiáveis, rápidos e mantidos. Testes flaky ensinam a equipe a ignorar alertas; checks duplicados aumentam fila sem reduzir risco. Proteção de branch também não prova que o teste cobre o comportamento certo. Defina responsáveis, tempos-alvo e caminho de exceção auditável para incidentes.

## Como verificar
Abra uma mudança deliberadamente incompatível e confirme que o check correspondente falha e bloqueia o merge. Teste mudanças fora do escopo dos filtros, falhas de infraestrutura e renomeação de jobs. Meça duração, taxa de flakiness e falsos bloqueios; revise gates quando a arquitetura ou os riscos mudarem.

## Conexões
- [[contract-testing-consumer-provider]] — transforma compatibilidade entre serviços em um check executável.
- [[migracoes-expand-contract]] — mudanças de schema pedem gates e sequenciamento próprios.
- [[sli-slo-orcamento-de-erro]] — confiabilidade em produção pode orientar a política de release.

## Fontes
- [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) — requisitos que podem proteger branches; acesso em 2026-10-01.
- [GitHub Docs — Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) — configuração de pull requests e status checks; acesso em 2026-10-01.
