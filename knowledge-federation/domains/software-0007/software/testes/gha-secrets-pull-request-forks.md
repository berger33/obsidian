---
id: software.testes.tranche08.000223
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
fontes: ["https://docs.github.com/en/actions/reference/security/secure-use", "https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitHub Actions: proteger secrets em pull requests externos

## Em uma frase
Evite expor secrets a código de pull request não confiável e escolha evento com contexto de segurança compreendido.

## Por que importa
Código de fork pode alterar workflow ou executar comandos que leem credenciais disponíveis no job.

## Como funciona
Separe validação sem segredo de deploy privilegiado, proteja ambientes e revise gatilhos como pull_request_target com cuidado especial.

## Exemplo
PR de fork roda lint e testes sem credenciais; publicação de release ocorre apenas após merge e aprovação em ambiente protegido.

## Limites e trade-offs
Evento diferente muda permissões e contexto de checkout; uma configuração superficial pode executar código não confiável com privilégio do repositório base.

## Como verificar
Use fork de teste, confirme valores mascarados não ficam acessíveis e revise checkout/ref e qualquer artefato consumido pelo job privilegiado.

## Conexões
- [[gha-environment-protection-gates]] — Veja também: GitHub Actions: verificar gates de environment antes do deploy.
- [[gha-script-injection-event-context]] — Veja também: GitHub Actions: evitar injeção em scripts com contexto de evento.

## Fontes
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
- [GitHub Actions — Managing environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) — protection rules, secrets e gates por ambiente; consultado em 2026-10-02.
