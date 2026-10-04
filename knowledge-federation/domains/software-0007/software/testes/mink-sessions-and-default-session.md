---
id: software.testes.tranche25.001873
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/minkphp/Mink/master/README.md", "https://mink.behat.org/en/latest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Registro de múltiplas sessões e setDefaultSessionName

## Em uma frase
O Usage Example do README oficial demonstra a inicialização do gerenciador: instancia-se new Mink(array('goutte1' => new Session(new GoutteDriver(new GoutteClient())), 'goutte2' => new Session(...), 'custom' => new Session(new MyCustomDriver($startUrl)))) e define-se a sessão padrão com $mink->setDefaultSessionName('goutte2').

## Por que importa
Centralizar várias instâncias de Session num único objeto Mink permite que o mesmo teste alterne entre drivers diferentes ou entre sessões independentes do mesmo driver usando apenas nomes simbólicos.

## Como funciona
Registre no construtor do Mink todas as sessões que o teste pode usar, configure uma delas com setDefaultSessionName e chame getSession() sem argumentos para o fluxo principal ou getSession('nome') quando precisar de outra sessão.

## Exemplo
No exemplo do README, após $mink->setDefaultSessionName('goutte2'), qualquer chamada a $mink->getSession() sem parâmetro retorna sempre a sessão 'goutte2', enquanto $mink->getSession('custom') acessa especificamente a sessão com MyCustomDriver.

## Limites e trade-offs
Chamar getSession() sem argumentos antes de definir setDefaultSessionName não tem sessão padrão para devolver; configure o nome padrão logo na inicialização do gerenciador.

## Como verificar
Conferi o bloco Usage Example completo no README oficial do repositório minkphp/Mink.

## Conexões
- [[mink-eight-drivers-catalog]] — Veja também: O catálogo de oito drivers na documentação e a dupla recomendada.
- [[mink-mixing-sessions-multiuser]] — Veja também: Misturar sessões no mesmo teste para simular múltiplos usuários.

## Fontes
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
