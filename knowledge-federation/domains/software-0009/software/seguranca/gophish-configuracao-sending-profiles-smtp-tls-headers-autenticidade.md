---
id: software.seguranca.tranche13.001242
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

# Configuração de **Sending Profiles (Perfis SMTP)** e Cabeçalhos Customizados (`X-Phish-Test`) no Gophish: Entregabilidade, SPF/DKIM/DMARC e Autorização

## Em uma frase
Para que uma campanha educativa de simulação de phishing chegue na caixa de entrada dos colaboradores sem ser bloqueada por servidores externos ou confundida pelo SOC com um ataque real não autorizado, como configurar corretamente o **Sending Profile (*Perfil de Envio SMTP*)** no Gophish?

## Por que importa
No módulo **Sending Profiles** do Gophish, você configura o servidor de disparo **`Host` (`smtp.dominio-simulacao.com:587` com STARTTLS/TLS)**, as credenciais de autenticação SMTP, o remetente `From` e, crucialmente, os **Custom Headers (*Cabeçalhos de E-mail Customizados*)**!

## Como funciona
Em simulações corporativas internas (*White-Box / Conscientização*), adicione um cabeçalho customizado secreto acordado com a equipe de infraestrutura de e-mail (por exemplo: **`X-Corp-Phish-Simulation: token-secreto-2026-q4`**) e configure a regra de *Authorized Phishing Simulation* no Microsoft Defender for Office 365 / Google Workspace / Proofpoint para permitir apenas e-mails originados do IP do servidor Gophish **E** que contenham esse cabeçalho exato! Já em exercícios de **Red Team (*Black-Box*)**, configure nos registros DNS do domínio contratado para a operação registros **SPF, DKIM e DMARC** impecáveis para testar a eficácia real dos filtros de e-mail da organização!

## Exemplo
```bash
# Verificar registros SPF, DKIM e DMARC de um dominio dedicado de simulacao antes de usa-lo no Sending Profile do Gophish
dig +short TXT dominio-simulacao.exemplo.br
dig +short TXT _dmarc.dominio-simulacao.exemplo.br
```

## Limites e trade-offs
Use sempre o botão **"Send Test Email"** dentro da tela do Sending Profile do Gophish antes de lançar qualquer campanha para validar a conexão TLS SMTP, a renderização HTML e os cabeçalhos recebidos.

## Como verificar
Jamais crie regras de *allowlist* no servidor de e-mail corporativo baseadas apenas no domínio `From` ou apenas no cabeçalho HTTP sem validar simultaneamente o **IP de origem do servidor Gophish** — caso contrário, um atacante externo que descobrisse o nome do cabeçalho poderia tentar explorar a regra de bypass!

## Conexões
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Veja também: Arquitetura do **Gophish (`gophish/gophish`)**: Plataforma Open-Source de Simulação de Phishing, Red Team e Treinamento de Conscientização em Segurança.
- [[gophish-templates-email-variaveis-dinamicas-tracking-pixel-links]] — Veja também: Engenharia de **Email Templates** no Gophish: Variáveis de Template (`{{.FirstName}}`, `{{.URL}}`, `{{.Tracker}}`), Importação de E-mail Original (`RFC 5322`) e Anexos.
- [[gophish-execucao-campanhas-agendamento-send-by-date-throttling]] — Referência cruzada direta com gophish-execucao-campanhas-agendamento-send-by-date-throttling.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
