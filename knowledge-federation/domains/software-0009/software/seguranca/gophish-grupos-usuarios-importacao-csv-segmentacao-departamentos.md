---
id: software.seguranca.tranche13.001245
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/gophish/gophish/master/README.md", "https://docs.getgophish.com/user-guide/documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gerenciamento de **Users & Groups** no Gophish: Importação em Lote via CSV e Segmentação de Campanhas por Perfil de Risco (`Position`)

## Em uma frase
Em vez de disparar o mesmo e-mail genérico para 5.000 funcionários de uma só vez, programas maduros de segurança da informação segmentam os exercícios de simulação por **departamento e superfície de ameaça real** (por exemplo: campanhas de fraude de fatura/boleto para o **Financeiro**, campanhas de currículo/anexo para o **RH**, campanhas de token OAuth/GitHub/CI-CD para **Engenharia de Software** e campanhas de Spearfishing para a **Diretoria Executiva**!).

## Por que importa
No módulo **Users & Groups** do Gophish, você cria grupos segmentados manualmente ou via **"Bulk Import Users"** enviando um arquivo `.csv` padronizado com exatamente quatro cabeçalhos de coluna: **`First Name`**, **`Last Name`**, **`Email`** e **`Position`**!

## Como funciona
O campo **`Position`** é duplamente estratégico: além de poder ser usado como variável dinâmica `{{.Position}}` dentro do texto do e-mail ou da Landing Page para aumentar o realismo do cenário, ele permite cruzar os resultados exportados da campanha por área de negócio para identificar quais departamentos precisam de reforço de treinamento específico (como adoção de chaves FIDO2/Passkeys)!

## Exemplo
```csv
First Name,Last Name,Email,Position
Ana,Silva,ana.silva@empresa.exemplo.br,Engenharia DevSecOps
Carlos,Mendes,carlos.mendes@empresa.exemplo.br,Financeiro Contas a Pagar
Marina,Costa,marina.costa@empresa.exemplo.br,Recursos Humanos
```

## Limites e trade-offs
Dica de automação: você pode sincronizar grupos de destinatários diretamente do seu diretório corporativo (Active Directory / Entra ID / Google Workspace / Keycloak) para o Gophish usando a API REST `/api/groups/` em um script Python antes de cada ciclo trimestral de treinamento.

## Como verificar
Sempre inclua no topo de cada grupo uma conta de controle da própria equipe de Segurança (`canary@empresa.exemplo.br`) para confirmar visualmente o recebimento e a formatação logo nos primeiros minutos do disparo.

## Conexões
- [[gophish-landing-pages-captura-credenciais-redirecionamento-educativo]] — Veja também: Criação de **Landing Pages** Éticas no Gophish: Clonagem de Site, **`Capture Submitted Data`**, Privacidade de Senhas e Redirecionamento Educativo (*Teachable Moment*).
- [[gophish-execucao-campanhas-agendamento-send-by-date-throttling]] — Veja também: Orquestração de **Campaigns** no Gophish: Cadência de Disparo (**`Send Emails By`**), Prevenção de *Rate-Limiting* SMTP e Escalonamento Temporal.
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-templates-email-variaveis-dinamicas-tracking-pixel-links]] — Referência cruzada direta com gophish-templates-email-variaveis-dinamicas-tracking-pixel-links.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
