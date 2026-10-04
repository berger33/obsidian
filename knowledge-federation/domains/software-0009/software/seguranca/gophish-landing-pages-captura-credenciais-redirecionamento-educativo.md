---
id: software.seguranca.tranche13.001244
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

# Criação de **Landing Pages** Éticas no Gophish: Clonagem de Site, **`Capture Submitted Data`**, Privacidade de Senhas e Redirecionamento Educativo (*Teachable Moment*)

## Em uma frase
Quando o colaborador clica no link `{{.URL}}` do e-mail simulado, ele chega à **Landing Page** hospedada pelo `phish_server` do Gophish. Como configurar a Landing Page para medir se o colaborador chegaria ao ponto de digitar suas credenciais **sem violar a privacidade nem armazenar senhas reais dos funcionários no banco de dados da simulação**?

## Por que importa
Na configuração de uma **Landing Page** no Gophish, existem três controles críticos que você deve conhecer profundamente: **(1) `Capture Submitted Data`** — quando marcado, o Gophish intercepta o `POST` do formulário HTML (`<form method="POST">`) e registra que o usuário submeteu dados (capturando os campos não-senha como o nome de usuário/e-mail); **(2) `Capture Passwords`** — uma caixa **separada e desmarcada por padrão** que controla se os campos `<input type="password">` serão salvos ou descartados!; e **(3) `Redirect to:`** — a URL para onde o usuário é redirecionado imediatamente após submeter o formulário!

## Como funciona
Em programas corporativos de conscientização e conformidade (ISO 27001 / PCI-DSS / LGPD), a prática recomendada é: **marcar `Capture Submitted Data`, DEIXAR DESMARCADO `Capture Passwords` (para que nenhuma senha real jamais seja gravada no banco do Gophish!) e configurar `Redirect to:` apontando para uma página educativa interna (*Teachable Moment*)** que explica em 3 pontos visuais quais sinais de phishing estavam presentes naquele e-mail!

## Exemplo
```html
<!-- Exemplo de formulario em uma Landing Page do Gophish: method="POST" com action="" envia a submissao para o proprio Gophish -->
<form action="" method="POST">
  <input type="email" name="username" placeholder="E-mail corporativo" required />
  <input type="password" name="password" placeholder="Senha" required />
  <button type="submit">Entrar</button>
</form>
```

## Limites e trade-offs
Por que o modelo de **Momento Educativo Imediato (*Just-in-Time Training*)** via `Redirect to:` após a submissão tem resultados muito melhores do que treinamentos anuais teóricos? Porque o colaborador recebe o feedback construtivo e visual no exato segundo em que cometeu o deslize, fixando o aprendizado imediatamente sem punição!

## Como verificar
Para que o Gophish capture o envio do formulário, garanta sempre que a tag `<form>` na Landing Page tenha `method="POST"` e que todos os campos `<input>` possuam o atributo `name="..."`.

## Conexões
- [[gophish-templates-email-variaveis-dinamicas-tracking-pixel-links]] — Veja também: Engenharia de **Email Templates** no Gophish: Variáveis de Template (`{{.FirstName}}`, `{{.URL}}`, `{{.Tracker}}`), Importação de E-mail Original (`RFC 5322`) e Anexos.
- [[gophish-grupos-usuarios-importacao-csv-segmentacao-departamentos]] — Veja também: Gerenciamento de **Users & Groups** no Gophish: Importação em Lote via CSV e Segmentação de Campanhas por Perfil de Risco (`Position`).
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-hardening-opsec-infraestrutura-gophish-headers-rid-customizado]] — Referência cruzada direta com gophish-hardening-opsec-infraestrutura-gophish-headers-rid-customizado.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
