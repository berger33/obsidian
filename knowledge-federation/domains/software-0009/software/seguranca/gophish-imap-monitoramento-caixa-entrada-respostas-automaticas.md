---
id: software.seguranca.tranche13.001249
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

# Monitoramento **IMAP** de Caixa de Entrada no Gophish: Detectando Respostas Diretas dos Usuários e Auto-Replies (*Out-of-Office*)

## Em uma frase
Em qualquer campanha de simulação de phishing ou operação de Red Team, o que acontece quando um colaborador desconfiado (ou prestativo!) decide **responder diretamente por e-mail (`Reply`)** ao endereço do remetente da campanha perguntando *"Olá, esse link do portal está correto?"*, ou quando dezenas de caixas de entrada enviam respostas automáticas de férias (**Out-of-Office / Auto-Reply**)?

## Por que importa
Se ninguém monitorar a caixa de entrada associada ao domínio de envio da campanha, o operador perde sinais valiosíssimos de interação humana (e, pior, mensagens de *Out-of-Office* às vezes revelam nomes de substitutos internos, telefones e estrutura hierárquica da empresa!).

## Como funciona
Na configuração de conta do Gophish (**Account Settings -> Reporting / IMAP Settings**), você pode conectar o Gophish via **IMAP sobre TLS (` porta 993`)** diretamente à caixa de correio do domínio da campanha para que ele verifique periodicamente (`IMAP Frequency`) novas mensagens recebidas associadas à operação!

## Exemplo
```bash
# Testar conectividade TLS com o servidor IMAP (porta 993) antes de configurar o monitoramento IMAP no Gophish
openssl s_client -connect imap.dominio-simulacao.exemplo.br:993 -crlf -quiet </dev/null
```

## Limites e trade-offs
Em exercícios de **Red Team**, audite também se as respostas automáticas de férias (*Out-of-Office*) de contas corporativas estão configuradas para responder para remetentes externos desconhecidos — bloquear *Auto-Replies* para fora da organização é uma medida simples de **OPSEC defensiva** que impede que atacantes mapeiem quem está de férias e quem é o aprovador substituto!

## Como verificar
Use sempre TLS (`Port 993`, `Use TLS = true`) e credenciais exclusivas de aplicação ao configurar o monitoramento IMAP no Gophish.

## Conexões
- [[gophish-webhooks-integracao-soar-slack-automacao-api-rest]] — Veja também: Automação em Tempo Real com **Webhooks Autenticados (`HMAC-SHA256`)** e **API REST** no Gophish: Integrando Simulações ao SOAR e Treinamento.
- [[gophish-hardening-opsec-infraestrutura-gophish-headers-rid-customizado]] — Veja também: OPSEC e Hardening de Infraestrutura **Gophish** para Red Teams: Customizando o Parâmetro `rid`, Cabeçalhos `X-Gophish` e Proteção com Proxy Reverso.
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade]] — Referência cruzada direta com gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade.
- [[openssl-diagnostico-tls-s-client-certificados-ciphers-alpn-ocsp]] — Referência cruzada direta com openssl-diagnostico-tls-s-client-certificados-ciphers-alpn-ocsp.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
