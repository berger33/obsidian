---
id: software.seguranca.hashing-senhas.000001
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html", "https://www.rfc-editor.org/rfc/rfc9106.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
aliases: [Hash de senhas, Argon2id, armazenamento de credenciais]
lote: software-seguranca-0003
---

# Armazenamento de senhas com hashing adaptativo

## Em uma frase
Uma aplicação deve armazenar um verificador de senha produzido por uma função lenta e adequada a senhas, nunca a senha em texto claro nem um hash criptográfico rápido usado isoladamente.

## Por que importa
Se uma cópia do banco de dados vazar, o atacante pode tentar adivinhar senhas offline. Funções rápidas como SHA-256 permitem testar muitas tentativas por segundo e não foram projetadas para esse uso. Um algoritmo de hashing adaptativo aumenta o custo de cada tentativa; isso não torna uma senha fraca impossível de adivinhar, mas pode tornar o ataque em larga escala mais caro.

## Como funciona
A OWASP recomenda Argon2id para novos sistemas e publica parâmetros mínimos, incluindo 19 MiB de memória, duas iterações e paralelismo 1 no momento desta verificação. Esses números são uma referência de configuração, não uma regra universal: a equipe deve medir o custo no ambiente real e acompanhar mudanças de orientação. A função usa um salt único por senha; bibliotecas maduras normalmente geram e armazenam esse salt junto aos parâmetros e ao resultado codificado. A RFC 9106 especifica Argon2 e seus parâmetros. Em autenticações futuras, a aplicação calcula o verificador com a biblioteca e parâmetros registrados e compara o resultado pelo mecanismo seguro da própria biblioteca.

## Exemplo
Uma biblioteca cria um hash codificado que contém identificador de algoritmo, parâmetros, salt e resultado. No login, o sistema verifica a senha apresentada com esse registro. Se os parâmetros antigos estiverem abaixo da política atual, uma autenticação bem-sucedida pode disparar uma atualização transparente do hash, desde que a senha original esteja disponível naquele momento.

## Limites e trade-offs
Hashing não é criptografia reversível e não permite recuperar a senha original; redefinição é preferível a recuperação. Mais memória e tempo elevam o custo também para o serviço legítimo, podendo afetar latência e disponibilidade se houver muitas verificações simultâneas. Não implemente algoritmos criptográficos próprios nem fixe parâmetros sem teste de capacidade. Salt não é segredo, e um “pepper” opcional exige gestão de segredo separada; nenhum deles compensa senhas previsíveis ou falta de controles contra tentativas online.

## Como verificar
Confira que o banco não contém senhas em claro, que cada registro usa uma função aprovada e salt distinto, e que o formato permite identificar parâmetros para migrações. Meça latência e memória sob carga de login, teste atualização de hashes legados e confirme que erros de autenticação não revelam se uma conta existe.

## Conexões
- [[csrf-token-protecao-web]] — armazenamento seguro de credenciais e proteção das ações autenticadas são controles complementares.
- [[gates-de-qualidade-no-merge]] — revisões automatizadas podem procurar regressões de configuração, mas precisam de testes específicos para autenticação.

## Fontes
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — algoritmos, salting e parâmetros de referência; acesso em 2026-10-01.
- [RFC 9106 — Argon2 Memory-Hard Function for Password Hashing and Proof-of-Work Applications](https://www.rfc-editor.org/rfc/rfc9106.html) — especificação do Argon2; acesso em 2026-10-01.
