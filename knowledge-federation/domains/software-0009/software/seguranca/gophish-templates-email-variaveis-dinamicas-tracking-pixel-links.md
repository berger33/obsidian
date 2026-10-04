---
id: software.seguranca.tranche13.001243
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

# Engenharia de **Email Templates** no Gophish: Variáveis de Template (`{{.FirstName}}`, `{{.URL}}`, `{{.Tracker}}`), Importação de E-mail Original (`RFC 5322`) e Anexos

## Em uma frase
Como o Gophish personaliza cada e-mail enviado para milhares de destinatários de áreas diferentes e sabe exatamente quais destinatários abriram o e-mail e quais clicaram no link?

## Por que importa
O motor de **Email Templates** do Gophish utiliza a sintaxe de templates do Go (`html/template`) para injetar variáveis dinâmicas específicas de cada destinatário no assunto (*Subject*), no corpo texto/HTML e até no endereço do remetente: **`{{.FirstName}}`**, **`{{.LastName}}`**, **`{{.Email}}`**, **`{{.Position}}`** (cargo/departamento), **`{{.From}}`**, **`{{.RId}}`** (o *Result ID* único daquele destinatário na campanha), **`{{.URL}}`** (a URL da Landing Page já parametrizada com `?rid={{.RId}}`) e **`{{.Tracker}}`** (que injeta uma tag `<img>` invisível de 1x1 pixel apontando para `{{.BaseURL}}/track?rid={{.RId}}`)!

## Como funciona
Além disso, o recurso **"Import Email"** permite colar o código-fonte bruto (` Raw / RFC 5322`) de qualquer e-mail real (com todo o seu layout CSS corporativo) e marcar **"Change Links to Point to Landing Page"**, convertendo automaticamente todos os links `<a href="...">` do e-mail para `{{.URL}}`!

## Exemplo
```html
<!-- Exemplo de Email Template educativo no Gophish utilizando variaveis dinamicas por destinatario e pixel de rastreamento -->
<html>
  <body>
    <p>Olá {{.FirstName}} {{.LastName}} ({{.Position}}),</p>
    <p>Solicitamos a revisão cadastral anual através do portal interno:</p>
    <p><a href="{{.URL}}">Acessar Portal de Revisão</a></p>
    {{.Tracker}}
  </body>
</html>
```

## Limites e trade-offs
Atenção ao interpretar a métrica **"Email Opened" (`{{.Tracker}}`)** em relatórios modernos: clientes de e-mail corporativos (como Outlook e Gmail) podem bloquear imagens remotas por padrão (fazendo com que um e-mail lido não dispare o pixel até o clique) ou usar *Image Proxies* (como Apple Mail Privacy Protection) que pré-carregam todas as imagens automaticamente! Por isso, a métrica definitiva de interação humana é sempre **"Clicked Link"** e **"Submitted Data"**!

## Como verificar
Sempre marque a caixa **"Add Tracking Image"** ou inclua `{{.Tracker}}` antes da tag `</body>` se quiser contabilizar aberturas de imagem.

## Conexões
- [[gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade]] — Veja também: Configuração de **Sending Profiles (Perfis SMTP)** e Cabeçalhos Customizados (`X-Phish-Test`) no Gophish: Entregabilidade, SPF/DKIM/DMARC e Autorização.
- [[gophish-landing-pages-captura-credenciais-redirecionamento-educativo]] — Veja também: Criação de **Landing Pages** Éticas no Gophish: Clonagem de Site, **`Capture Submitted Data`**, Privacidade de Senhas e Redirecionamento Educativo (*Teachable Moment*).
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-relatorios-eventos-email-reportado-rid-metricas-soc]] — Referência cruzada direta com gophish-relatorios-eventos-email-reportado-rid-metricas-soc.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
