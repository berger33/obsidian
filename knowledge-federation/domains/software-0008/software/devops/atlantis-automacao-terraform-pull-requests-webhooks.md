---
id: software.devops.tranche10.000941
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md", "https://www.runatlantis.io/docs/using-atlantis.html", "https://www.runatlantis.io/docs/locking.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Atlantis: automação self-hosted de fluxos Terraform em Pull Requests via webhooks

## Em uma frase
O **Atlantis** (`runatlantis/atlantis`) é uma aplicação Go auto-hospedada (self-hosted) que escuta eventos de Pull Request/Merge Request via webhooks do Git, executa `terraform plan`, `import` e `apply` remotamente e comenta o resultado de volta diretamente no Pull Request.

## Por que importa
Quando engenheiros executam `terraform apply` de suas máquinas locais, ninguém na equipe vê o plano que foi aplicado, estados ficam dessincronizados com a branch `main` e credenciais administrativas da nuvem precisam ser distribuídas nos laptops dos desenvolvedores. Segundo o README oficial (`What is Atlantis?` / `Why should you use it?`), o Atlantis torna as mudanças de Terraform visíveis para toda a equipe, permite colaboração segura e padroniza os fluxos de IaC.

## Como funciona
O servidor Atlantis roda dentro da infraestrutura da própria empresa (por exemplo, como um Deployment/StatefulSet no Kubernetes ou container ECS com uma IAM Role da nuvem) conectado por webhook ao GitHub, GitLab, Bitbucket ou Azure DevOps: (1) quando um engenheiro abre ou atualiza um Pull Request alterando arquivos `.tf`, o Atlantis recebe o webhook, clona o PR, executa **`terraform plan`** automaticamente (**Autoplanning**) e posta a saída completa do plano em um comentário no PR; (2) a equipe revisa o código e o plano no próprio PR; e (3) após a aprovação humana do PR, comentar **`atlantis apply`** instrui o Atlantis a aplicar exatamente aquele plano salvo (`$PLANFILE`), postar o resultado do `apply` e opcionalmente fazer o merge automático do PR (**Automerging**).

## Exemplo
```text
# Comentários de Pull Request reconhecidos pelo Atlantis conforme a documentação Using Atlantis
atlantis help
atlantis version
atlantis plan
atlantis apply
```

## Limites e trade-offs
Como o Atlantis aplica as mudanças no ambiente real **antes** que o Pull Request seja mergeado na branch `main` (para garantir que, se o `terraform apply` falhar no meio do caminho, o engenheiro possa corrigir na mesma branch do PR e re-executar `atlantis plan`/`apply` sem deixar a `main` quebrada), é obrigatório utilizar o sistema de **Locking** do Atlantis e fazer o merge do PR imediatamente após o `apply` bem-sucedido.

## Como verificar
Comente `atlantis version` ou `atlantis help` em um Pull Request de teste conectado ao servidor Atlantis e verifique que o bot responde em segundos com a versão do Terraform configurada.

## Conexões
- [[atlantis-comandos-pull-request-plan-apply-flags-workspaces]] — Veja também: Atlantis: comandos de comentário em PR (atlantis plan e apply), seleção de projeto (-d, -p, -w) e arquivos env/{workspace}.tfvars.
- [[atlantis-bloqueio-diretorio-workspace-locking-unlock]] — Referência cruzada direta com atlantis-bloqueio-diretorio-workspace-locking-unlock.
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/locking.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
