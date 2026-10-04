---
id: software.testes.tranche23.001722
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://boofuzz.readthedocs.io/en/stable/user/quickstart.html", "https://github.com/jtpereyda/boofuzz/blob/master/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Requests com String, Delim e Static: o protocolo como AST

## Em uma frase
Após ler o RFC, a página manda "define your protocol using the various block and primitive types": cada mensagem é um Request nomeado cujos filhos descrevem a estrutura, e o exemplo do FTP constrói user, pass, stor e retr idênticos — String para os campos mutáveis, Delim("space", " ") como separador e Static("end", ...) com o terminator CRLF da linha.

## Por que importa
A gramática torna o alvo do mutator explícito: o boofuzz muda Strings e campos tipados e respeita Statics — o que separa fuzzing de protocolo de despejo de bytes aleatórios na porta, e é o núcleo da promessa "easy and quick data generation" do README.

## Como funciona
A forma canônica vista na página é Request("user", children=(String("key", "USER"), Delim("space", " "), String("val", "anonymous"), Static("end", cr-lf))) — quatro primitivas por linha, uma Request por comando do protocolo.

## Exemplo
Declare dois Requests para um protocolo textual qualquer com Delim e Static como no exemplo e imprima a renderização estática (sem fuzz): o bytes gerado deve ser um pacote do protocolo válido de verdade.

## Limites e trade-offs
A página apresenta o mínimo, não a taxonomia — tipos numéricos, Block com endianness, checksums e demais primitivas vivem na página de protocol definition (para onde a doc aponta com "various block and primitive types"), que a Quickstart não repete.

## Como verificar
Abra a seção de definição de mensagens do Quickstart e o link de destino block/primitive types referenciado por ela; confira o snippet FTP integral.

## Conexões
- [[boofuzz-session-target]] — Veja também: Session é o centro; Target carrega a conexão.
- [[boofuzz-state-graph]] — Veja também: O grafo de Requests decide a ordem do fuzzing.

## Fontes
- [boofuzz — Quickstart (Read the Docs)](https://boofuzz.readthedocs.io/en/stable/user/quickstart.html) — Session, Target, conexões, Requests, grafo, resultados e exemplos; consultado em 2026-10-03.
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.
